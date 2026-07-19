"""SRT subtitle file parser and writer"""

from typing import List, Dict
from pathlib import Path
import re
import logging

logger = logging.getLogger(__name__)


class SRTParser:
    """Parse SRT subtitle files"""

    @staticmethod
    def parse(srt_file: str) -> List[Dict]:
        """
        Parse SRT file

        Args:
            srt_file: Path to SRT file

        Returns:
            List of subtitle segments

        Example:
            segments = SRTParser.parse("subtitles.srt")
            # [
            #   {"id": 1, "start": "00:00:00,500", "end": "00:00:07,000", "text": "Hello"},
            #   ...
            # ]
        """
        segments = []
        try:
            with open(srt_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Split by double newline
            blocks = content.strip().split("\n\n")

            for block in blocks:
                lines = block.strip().split("\n")
                if len(lines) >= 3:
                    segment = {
                        "id": int(lines[0]),
                        "start": lines[1].split(" --> ")[0],
                        "end": lines[1].split(" --> ")[1],
                        "text": "\n".join(lines[2:]),
                    }
                    segments.append(segment)

            logger.info(f"✅ Parsed {len(segments)} segments from {srt_file}")
            return segments
        except Exception as e:
            logger.error(f"Error parsing SRT: {e}")
            raise


class SRTWriter:
    """Write SRT subtitle files"""

    @staticmethod
    def write(segments: List[Dict], output_file: str):
        """
        Write segments to SRT file

        Args:
            segments: List of subtitle segments
            output_file: Output SRT file path
        """
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                for i, segment in enumerate(segments, 1):
                    f.write(f"{i}\n")
                    f.write(f"{segment['start']} --> {segment['end']}\n")
                    f.write(f"{segment.get('translated_text', segment['text'])}\n")
                    f.write("\n")

            logger.info(f"✅ SRT written: {output_file}")
        except Exception as e:
            logger.error(f"Error writing SRT: {e}")
            raise