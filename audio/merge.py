"""Merge/replace audio in video file"""

import subprocess
from pathlib import Path
from typing import Optional
import logging

logger = logging.getLogger(__name__)


def merge_audio_to_video(
    input_video: str,
    input_audio: str,
    output_video: Optional[str] = None,
    codec: str = "h264",
    preset: str = "medium",
) -> str:
    """
    Merge audio with video (replace audio track)

    Args:
        input_video: Path to input video file
        input_audio: Path to input audio file
        output_video: Path to output video file (auto-generated if None)
        codec: Video codec (h264, h265, libvpx, etc.)
        preset: Encoding preset (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow)

    Returns:
        Path to output video file

    Raises:
        FileNotFoundError: If input files not found
        subprocess.CalledProcessError: If FFmpeg fails
    """
    video_path = Path(input_video)
    audio_path = Path(input_audio)

    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {input_video}")
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {input_audio}")

    if output_video is None:
        output_video = video_path.stem + "_dubbed.mp4"

    logger.info(f"Merging audio into video...")

    cmd = [
        "ffmpeg",
        "-i",
        str(input_video),
        "-i",
        str(input_audio),
        "-c:v",
        codec,
        "-preset",
        preset,
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-map",
        "0:v:0",  # Map video from first input
        "-map",
        "1:a:0",  # Map audio from second input
        "-shortest",  # End at shortest stream
        "-y",  # Overwrite output
        str(output_video),
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        logger.info(f"✅ Video with new audio saved: {output_video}")
        return output_video
    except subprocess.CalledProcessError as e:
        logger.error(f"FFmpeg error: {e.stderr.decode()}")
        raise