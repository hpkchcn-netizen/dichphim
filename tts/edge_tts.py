"""Microsoft Edge TTS (Online)"""

import edge_tts
import asyncio
from typing import List, Optional
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class EdgeTTS:
    """Microsoft Edge Text-to-Speech Engine"""

    def __init__(self, voice: str = "vi-VN-HoaiMyNeural"):
        """
        Initialize Edge TTS

        Args:
            voice: Voice to use (e.g., 'vi-VN-HoaiMyNeural', 'en-US-AriaNeural')
        """
        self.voice = voice
        logger.info(f"Initialized Edge TTS with voice: {voice}")

    async def _text_to_speech_async(
        self,
        text: str,
        output_file: str,
        rate: str = "+0%",
        volume: str = "+0%",
    ) -> str:
        """
        Internal async TTS

        Args:
            text: Text to synthesize
            output_file: Output audio file path
            rate: Speed rate (e.g., '+10%', '-20%')
            volume: Volume (e.g., '+10%')

        Returns:
            Path to output file
        """
        try:
            communicate = edge_tts.Communicate(
                text=text,
                voice=self.voice,
                rate=rate,
                volume=volume,
            )
            await communicate.save(output_file)
            logger.info(f"✅ TTS generated: {output_file}")
            return output_file
        except Exception as e:
            logger.error(f"TTS failed: {e}")
            raise

    def text_to_speech(
        self,
        text: str,
        output_file: str,
        rate: str = "+0%",
        volume: str = "+0%",
    ) -> str:
        """
        Convert text to speech

        Args:
            text: Text to convert
            output_file: Output audio file path
            rate: Speech rate
            volume: Volume level

        Returns:
            Path to audio file
        """
        logger.info(f"Generating speech from text ({len(text)} chars)...")
        return asyncio.run(
            self._text_to_speech_async(text, output_file, rate, volume)
        )

    def synthesize_segments(
        self,
        segments: List[dict],
        output_dir: str = "./temp",
    ) -> List[dict]:
        """
        Synthesize speech for subtitle segments

        Args:
            segments: List of segments with 'translated_text' field
            output_dir: Directory to save audio files

        Returns:
            Segments with 'audio_file' field added
        """
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        for i, segment in enumerate(segments):
            audio_file = output_path / f"segment_{i:04d}.mp3"
            self.text_to_speech(segment["translated_text"], str(audio_file))
            segment["audio_file"] = str(audio_file)
            logger.info(f"  [{i+1}/{len(segments)}] Audio: {segment['translated_text'][:50]}...")

        return segments