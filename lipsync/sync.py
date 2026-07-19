"""Lip synchronization using media foundation or audio analysis"""

import librosa
import numpy as np
from typing import List, Dict, Tuple
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class LipSync:
    """Lip synchronization engine"""

    def __init__(self, model_type: str = "simple"):
        """
        Initialize lip sync

        Args:
            model_type: Model type ('simple', 'advanced')
        """
        self.model_type = model_type
        logger.info(f"Initialized LipSync with model: {model_type}")

    @staticmethod
    def extract_audio_features(audio_file: str) -> Tuple[np.ndarray, int]:
        """
        Extract audio features for lip sync analysis

        Args:
            audio_file: Path to audio file

        Returns:
            Tuple of (MFCC features, sample rate)
        """
        try:
            # Load audio
            y, sr = librosa.load(audio_file, sr=None)

            # Extract MFCC (Mel-frequency cepstral coefficients)
            mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            logger.info(f"✅ Audio features extracted: {mfcc.shape}")
            return mfcc, sr
        except Exception as e:
            logger.error(f"Error extracting audio features: {e}")
            raise

    def analyze_speech_segments(self, audio_file: str) -> List[Dict]:
        """
        Analyze audio to identify speech segments

        Args:
            audio_file: Path to audio file

        Returns:
            List of speech segments with timing
        """
        logger.info(f"Analyzing speech segments in {audio_file}...")

        try:
            y, sr = librosa.load(audio_file, sr=None)

            # Detect speech using energy-based method
            S = librosa.feature.melspectrogram(y=y, sr=sr)
            S_db = librosa.power_to_db(S, ref=np.max)

            # Get energy over time
            energy = np.mean(S_db, axis=0)
            threshold = np.mean(energy) + 0.5 * np.std(energy)

            # Find frames above threshold
            speech_frames = np.where(energy > threshold)[0]

            # Convert frames to time
            times = librosa.frames_to_time(speech_frames, sr=sr)

            segments = []
            if len(times) > 0:
                start = times[0]
                for i in range(1, len(times)):
                    # New segment if gap > 0.5 seconds
                    if times[i] - times[i - 1] > 0.5:
                        segments.append(
                            {
                                "start": float(start),
                                "end": float(times[i - 1]),
                            }
                        )
                        start = times[i]
                # Add last segment
                segments.append({"start": float(start), "end": float(times[-1])})

            logger.info(f"✅ Found {len(segments)} speech segments")
            return segments
        except Exception as e:
            logger.error(f"Error analyzing speech: {e}")
            raise

    def calculate_sync_offset(
        self, original_audio: str, dubbed_audio: str
    ) -> float:
        """
        Calculate time offset between original and dubbed audio

        Args:
            original_audio: Path to original audio
            dubbed_audio: Path to dubbed audio

        Returns:
            Offset in seconds (positive = dubbed is ahead)
        """
        logger.info("Calculating sync offset...")

        try:
            # Load both audios
            y1, sr1 = librosa.load(original_audio, sr=None)
            y2, sr2 = librosa.load(dubbed_audio, sr=None)

            # Resample to same rate
            if sr1 != sr2:
                y2 = librosa.resample(y2, orig_sr=sr2, target_sr=sr1)

            # Calculate cross-correlation
            correlation = np.correlate(y1, y2, mode="same")
            offset_samples = np.argmax(correlation) - len(y1) // 2
            offset_seconds = offset_samples / sr1

            logger.info(f"✅ Sync offset: {offset_seconds:.3f} seconds")
            return offset_seconds
        except Exception as e:
            logger.error(f"Error calculating offset: {e}")
            raise