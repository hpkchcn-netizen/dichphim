"""Audio processing module"""

from .extract import extract_audio
from .merge import merge_audio_to_video
from .normalize import normalize_audio

__all__ = [
    "extract_audio",
    "merge_audio_to_video",
    "normalize_audio",
]