"""Time stretching and synchronization utilities"""

from typing import List, Dict, Tuple
import logging

logger = logging.getLogger(__name__)


class TimeStretch:
    """Time stretch audio and subtitle timing"""

    @staticmethod
    def seconds_to_timestamp(seconds: float) -> str:
        """
        Convert seconds to SRT timestamp format

        Args:
            seconds: Time in seconds

        Returns:
            Timestamp in HH:MM:SS,mmm format
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

    @staticmethod
    def timestamp_to_seconds(timestamp: str) -> float:
        """
        Convert SRT timestamp to seconds

        Args:
            timestamp: Timestamp in HH:MM:SS,mmm format

        Returns:
            Time in seconds
        """
        parts = timestamp.replace(",", ".").split(":")
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])

    @staticmethod
    def stretch_segment(
        segment: Dict,
        original_duration: float,
        target_duration: float,
    ) -> Dict:
        """
        Stretch timing of a segment

        Args:
            segment: Subtitle segment
            original_duration: Original duration in seconds
            target_duration: Target duration in seconds

        Returns:
            Segment with adjusted timing
        """
        if original_duration == 0:
            return segment

        ratio = target_duration / original_duration
        start = TimeStretch.timestamp_to_seconds(segment["start"])
        end = TimeStretch.timestamp_to_seconds(segment["end"])

        segment["start"] = TimeStretch.seconds_to_timestamp(start * ratio)
        segment["end"] = TimeStretch.seconds_to_timestamp(end * ratio)

        return segment