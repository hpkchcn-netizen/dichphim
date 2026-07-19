"""Main dubbing pipeline orchestration"""

import logging
from typing import Dict, Optional
from pathlib import Path

from translation.google_translate import GoogleTranslate
from tts.edge_tts import EdgeTTS
from subtitle.srt import SRTParser, SRTWriter
from subtitle.timing import TimeStretch
from video.ffmpeg_ops import FFmpegOps
from lipsync.sync import LipSync

logger = logging.getLogger(__name__)


class DubPipeline:
    """End-to-end dubbing pipeline"""

    def __init__(
        self,
        source_lang: str = "vi",
        target_lang: str = "en",
        voice: str = "en-US-AriaNeural",
    ):
        """
        Initialize dubbing pipeline

        Args:
            source_lang: Source language code
            target_lang: Target language code
            voice: TTS voice to use
        """
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translator = GoogleTranslate()
        self.tts = EdgeTTS(voice=voice)
        self.lipsync = LipSync()
        logger.info(
            f"Initialized DubPipeline: {source_lang} -> {target_lang} ({voice})"
        )

    def process_subtitles(self, srt_file: str, output_dir: str = "./temp") -> Dict:
        """
        Process subtitles: parse, translate, and generate audio

        Args:
            srt_file: Path to SRT subtitle file
            output_dir: Output directory for audio files

        Returns:
            Dict with processed segments
        """
        logger.info(f"Processing subtitles from {srt_file}...")

        # Parse SRT
        segments = SRTParser.parse(srt_file)
        logger.info(f"✓ Parsed {len(segments)} segments")

        # Translate and generate audio
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        for i, segment in enumerate(segments):
            # Translate
            translated = self.translator.translate(
                segment["text"], source_lang=self.source_lang, target_lang=self.target_lang
            )
            segment["translated_text"] = translated
            logger.info(f"  [{i+1}/{len(segments)}] Translated: {translated[:50]}...")

            # Generate speech
            audio_file = output_path / f"segment_{i:04d}.mp3"
            self.tts.text_to_speech(translated, str(audio_file))
            segment["audio_file"] = str(audio_file)

        logger.info(f"✓ Processed {len(segments)} segments")
        return {"segments": segments, "output_dir": output_dir}

    def analyze_video(self, video_file: str) -> Dict:
        """
        Analyze video file

        Args:
            video_file: Path to video file

        Returns:
            Dict with video metadata
        """
        logger.info(f"Analyzing video: {video_file}")
        info = FFmpegOps.get_video_info(video_file)
        duration = FFmpegOps.get_duration(video_file)
        logger.info(f"✓ Video duration: {duration:.2f}s")
        return {"info": info, "duration": duration}

    def sync_audio_timing(
        self, segments: list, video_duration: float
    ) -> list:
        """
        Synchronize audio timing with video

        Args:
            segments: List of subtitle segments
            video_duration: Original video duration in seconds

        Returns:
            Segments with adjusted timing
        """
        logger.info("Synchronizing audio timing...")

        original_end = 0
        if segments:
            original_end = TimeStretch.timestamp_to_seconds(segments[-1]["end"])

        if original_end > 0 and original_end != video_duration:
            stretch_ratio = video_duration / original_end
            logger.info(f"  Stretch ratio: {stretch_ratio:.3f}")

            for segment in segments:
                TimeStretch.stretch_segment(segment, original_end, video_duration)

        logger.info("✓ Timing synchronized")
        return segments

    def generate_output(self, segments: list, output_srt: str):
        """
        Generate output SRT file

        Args:
            segments: Processed segments
            output_srt: Output SRT file path
        """
        logger.info(f"Writing output to {output_srt}...")
        SRTWriter.write(segments, output_srt)
        logger.info(f"✓ Output generated")

    def run(
        self,
        video_file: str,
        srt_file: str,
        output_srt: str = "output.srt",
        temp_dir: str = "./temp",
    ) -> Dict:
        """
        Run complete dubbing pipeline

        Args:
            video_file: Input video file
            srt_file: Input subtitle file
            output_srt: Output subtitle file
            temp_dir: Temporary directory for audio files

        Returns:
            Pipeline results
        """
        logger.info("="*50)
        logger.info("Starting DUB PIPELINE")
        logger.info("="*50)

        try:
            # Step 1: Analyze video
            video_data = self.analyze_video(video_file)
            video_duration = video_data["duration"]

            # Step 2: Process subtitles
            subtitle_data = self.process_subtitles(srt_file, temp_dir)
            segments = subtitle_data["segments"]

            # Step 3: Synchronize timing
            segments = self.sync_audio_timing(segments, video_duration)

            # Step 4: Generate output
            self.generate_output(segments, output_srt)

            logger.info("="*50)
            logger.info("✓ PIPELINE COMPLETED")
            logger.info("="*50)

            return {
                "status": "success",
                "output_srt": output_srt,
                "audio_dir": temp_dir,
                "segments_count": len(segments),
            }
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            raise