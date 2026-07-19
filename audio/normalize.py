"""Normalize and adjust audio levels"""

import numpy as np
from pathlib import Path
from typing import Tuple
import logging

logger = logging.getLogger(__name__)


def normalize_audio(
    input_audio: str,
    output_audio: str,
    target_db: float = -20.0,
) -> str:
    """
    Normalize audio to target loudness

    Args:
        input_audio: Path to input audio
        output_audio: Path to output audio
        target_db: Target loudness in dB

    Returns:
        Path to normalized audio
    """
    logger.info(f"Normalizing audio to {target_db}dB...")

    try:
        from pydub import AudioSegment
        
        # Load audio
        audio = AudioSegment.from_file(input_audio)
        
        # Calculate current loudness
        current_db = audio.dBFS
        
        # Calculate gain needed
        gain_needed = target_db - current_db
        
        # Apply gain
        normalized = audio.apply_gain(gain_needed)
        
        # Export
        normalized.export(output_audio, format="wav")
        logger.info(f"✅ Audio normalized: {output_audio}")
        return output_audio
    except Exception as e:
        logger.error(f"Error normalizing audio: {e}")
        raise