"""FFmpeg video operations"""

import subprocess
from pathlib import Path
from typing import Optional, Dict, List
import logging
import json

logger = logging.getLogger(__name__)


class FFmpegOps:
    """FFmpeg wrapper for video operations"""

    @staticmethod
    def get_video_info(video_file: str) -> Dict:
        """
        Get video file information using ffprobe

        Args:
            video_file: Path to video file

        Returns:
            Dict with video metadata
        """
        cmd = [
            "ffprobe",
            "-v",
            "quiet",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            video_file,
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            info = json.loads(result.stdout)
            logger.info(f"✅ Video info retrieved: {video_file}")
            return info
        except Exception as e:
            logger.error(f"Error getting video info: {e}")
            raise

    @staticmethod
    def get_duration(video_file: str) -> float:
        """
        Get video duration in seconds

        Args:
            video_file: Path to video file

        Returns:
            Duration in seconds
        """
        try:
            info = FFmpegOps.get_video_info(video_file)
            duration = float(info["format"]["duration"])
            logger.info(f"Video duration: {duration:.2f} seconds")
            return duration
        except Exception as e:
            logger.error(f"Error getting duration: {e}")
            raise