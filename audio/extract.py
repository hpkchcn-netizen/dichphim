"""Extract audio from video file"""

import subprocess
from pathlib import Path
from typing import Optional
import logging

logger = logging.getLogger(__name__)


def extract_audio(
    input_video: str,
    output_audio: Optional[str] = None,
    audio_format: str = "wav",
    sample_rate: int = 16000,
    channels: int = 1,
) -> str:
    """
    Extract audio from video file using FFmpeg

    Args:
        input_video: Path to input video file
        output_audio: Path to output audio file (auto-generated if None)
        audio_format: Audio format (wav, mp3, flac, etc.)
        sample_rate: Sample rate in Hz
        channels: Number of channels (1=mono, 2=stereo)

    Returns:
        Path to extracted audio file

    Raises:
        FileNotFoundError: If input video not found
        subprocess.CalledProcessError: If FFmpeg fails
    """
    input_path = Path(input_video)
    if not input_path.exists():
        raise FileNotFoundError(f"Video file not found: {input_video}")

    if output_audio is None:
        output_audio = input_path.stem + f".{audio_format}"

    logger.info(f"Extracting audio from {input_video}...")

    cmd = [
        "ffmpeg",
        "-i",
        str(input_video),
        "-vn",  # No video
        "-acodec",
        "pcm_s16le" if audio_format == "wav" else "libmp3lame",
        "-ar",
        str(sample_rate),
        "-ac",
        str(channels),
        "-q:a",
        "9",  # Quality (0=best, 9=worst)
        "-y",  # Overwrite output
        str(output_audio),
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        logger.info(f"✅ Audio extracted: {output_audio}")
        return output_audio
    except subprocess.CalledProcessError as e:
        logger.error(f"FFmpeg error: {e.stderr.decode()}")
        raise