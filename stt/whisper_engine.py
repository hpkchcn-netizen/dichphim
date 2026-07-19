"""Whisper Speech Recognition Engine"""

import whisper
from typing import List, Dict, Optional
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class WhisperSTT:
    """OpenAI Whisper Speech-to-Text Engine"""

    def __init__(
        self,
        model_size: str = "large",
        device: str = "cuda",
        compute_type: str = "float16",
    ):
        """
        Initialize Whisper model

        Args:
            model_size: Model size (tiny, base, small, medium, large)
            device: Device to use (cuda, cpu)
            compute_type: Computation type (float16, int8)
        """
        self.model_size = model_size
        self.device = device
        self.compute_type = compute_type
        self.model = None
        self._load_model()

    def _load_model(self):
        """Load Whisper model"""
        logger.info(f"Loading Whisper {self.model_size} model...")
        try:
            self.model = whisper.load_model(
                self.model_size,
                device=self.device,
            )
            logger.info("✅ Whisper model loaded")
        except Exception as e:
            logger.error(f"Failed to load Whisper model: {e}")
            raise

    def transcribe(
        self,
        audio_file: str,
        language: Optional[str] = None,
        temperature: float = 0.0,
    ) -> Dict:
        """
        Transcribe audio file to text with timestamps

        Args:
            audio_file: Path to audio file
            language: Language code (auto-detect if None)
            temperature: Temperature for sampling

        Returns:
            Dict with segments containing {id, start, end, text}

        Example:
            result = whisper_stt.transcribe("audio.wav")
            # {
            #   "text": "Hello everyone. Today we...",
            #   "segments": [
            #     {"id": 0, "start": 0.2, "end": 2.8, "text": "Hello everyone."},
            #     {"id": 1, "start": 3.0, "end": 6.0, "text": "Today we..."}
            #   ],
            #   "language": "en"
            # }
        """
        audio_path = Path(audio_file)
        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_file}")

        logger.info(f"Transcribing {audio_file}...")

        try:
            options = {
                "temperature": temperature,
                "best_of": 5,
                "beam_size": 5,
            }
            if language:
                options["language"] = language

            result = self.model.transcribe(str(audio_path), **options)

            logger.info(
                f"✅ Transcription complete: {len(result['segments'])} segments"
            )
            logger.info(f"   Detected language: {result['language']}")
            logger.info(f"   Text: {result['text'][:100]}...")

            return result
        except Exception as e:
            logger.error(f"Transcription failed: {e}")
            raise

    def get_language(self, audio_file: str) -> str:
        """
        Detect language of audio file

        Args:
            audio_file: Path to audio file

        Returns:
            Language code (e.g., 'en', 'vi', 'zh')
        """
        try:
            import librosa

            # Load audio
            audio, sr = librosa.load(audio_file)
            # Get mel spectrogram
            mel = whisper.log_mel_spectrogram(audio)
            # Detect language
            _, probs = self.model.detect_language(mel)
            language = max(probs, key=probs.get)
            logger.info(f"Detected language: {language}")
            return language
        except Exception as e:
            logger.error(f"Language detection failed: {e}")
            return "en"  # Default to English