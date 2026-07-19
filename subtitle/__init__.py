"""Subtitle processing module"""

from .srt import SRTParser, SRTWriter
from .timing import TimeStretch

__all__ = ["SRTParser", "SRTWriter", "TimeStretch"]