"""Configuration file for DichPhim - Vietnamese Video Dubbing Tool"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# PROJECT SETTINGS
# ============================================================================

PROJECT_NAME = "DichPhim"
PROJECT_VERSION = "0.1.0"
PROJECT_ROOT = Path(__file__).parent
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# ============================================================================
# GOOGLE CLOUD TRANSLATION API
# ============================================================================

GOOGLE_CLOUD_PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT_ID", "")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS",
    str(PROJECT_ROOT / "credentials.json")
)

# Check if credentials file exists
if GOOGLE_APPLICATION_CREDENTIALS and not os.path.exists(GOOGLE_APPLICATION_CREDENTIALS):
    print(f"Warning: Google Cloud credentials not found at {GOOGLE_APPLICATION_CREDENTIALS}")

# ============================================================================
# TRANSLATION SETTINGS
# ============================================================================

SOURCE_LANGUAGE = os.getenv("SOURCE_LANGUAGE", "en")
TARGET_LANGUAGE = os.getenv("TARGET_LANGUAGE", "vi")

# Supported language pairs
SUPPORTED_LANGUAGES = {
    "en": "English",
    "vi": "Vietnamese",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
}

# ============================================================================
# TEXT-TO-SPEECH (EDGE TTS) SETTINGS
# ============================================================================

# Vietnamese TTS voices
TTS_VOICES = {
    "vi": "vi-VN-NhanNeural",
    "vi_female": "vi-VN-HoaiMyNeural",
}

TTS_RATE = os.getenv("TTS_RATE", "1.0")
TTS_PITCH = os.getenv("TTS_PITCH", "0")
TTS_VOLUME = os.getenv("TTS_VOLUME", "1.0")

# ============================================================================
# AUDIO SETTINGS
# ============================================================================

AUDIO_SAMPLE_RATE = int(os.getenv("AUDIO_SAMPLE_RATE", "48000"))
AUDIO_CHANNELS = int(os.getenv("AUDIO_CHANNELS", "2"))
AUDIO_CODEC = os.getenv("AUDIO_CODEC", "aac")
AUDIO_BITRATE = os.getenv("AUDIO_BITRATE", "192k")

# ============================================================================
# VIDEO SETTINGS
# ============================================================================

VIDEO_CODEC = os.getenv("VIDEO_CODEC", "libx264")
VIDEO_PRESET = os.getenv("VIDEO_PRESET", "medium")
VIDEO_CRF = int(os.getenv("VIDEO_CRF", "23"))
VIDEO_FORMATS = ["mp4", "mkv", "avi", "mov", "flv", "webm"]
MAX_VIDEO_RESOLUTION = (1920, 1080)

# ============================================================================
# SUBTITLE SETTINGS
# ============================================================================

SUBTITLE_FORMATS = ["srt", "vtt", "ass", "ssa"]
SUBTITLE_ENCODING = "utf-8"
SUBTITLE_DEFAULT_DURATION = 5.0

# ============================================================================
# LIP-SYNC SETTINGS
# ============================================================================

ENABLE_LIPSYNC = True
LIPSYNC_MODEL = os.getenv("LIPSYNC_MODEL", "default")
LIPSYNC_CONFIDENCE_THRESHOLD = float(os.getenv("LIPSYNC_CONFIDENCE_THRESHOLD", "0.7"))
FACE_DETECTION_MODEL = "mediapipe"

# ============================================================================
# PERFORMANCE SETTINGS
# ============================================================================

MAX_WORKERS = int(os.getenv("MAX_WORKERS", "4"))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "10"))
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1048576"))
TIMEOUT = int(os.getenv("TIMEOUT", "3600"))

# GPU/CPU settings
USE_GPU = os.getenv("USE_GPU", "False").lower() == "true"
GPU_DEVICE = int(os.getenv("GPU_DEVICE", "0"))

# ============================================================================
# PATHS AND DIRECTORIES
# ============================================================================

TEMP_DIR = Path(os.getenv("TEMP_DIR", PROJECT_ROOT / "temp"))
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", PROJECT_ROOT / "output"))
CACHE_DIR = Path(os.getenv("CACHE_DIR", PROJECT_ROOT / "cache"))
LOGS_DIR = Path(os.getenv("LOGS_DIR", PROJECT_ROOT / "logs"))

# Create directories if they don't exist
for directory in [TEMP_DIR, OUTPUT_DIR, CACHE_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# FFmpeg path
FFMPEG_PATH = os.getenv("FFMPEG_PATH", "ffmpeg")
FFPROBE_PATH = os.getenv("FFPROBE_PATH", "ffprobe")

# ============================================================================
# LOGGING SETTINGS
# ============================================================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = LOGS_DIR / "dichphim.log"
LOG_MAX_BYTES = 10 * 1024 * 1024
LOG_BACKUP_COUNT = 5

# ============================================================================
# API RATE LIMITING
# ============================================================================

TRANSLATION_API_RATE_LIMIT = int(os.getenv("TRANSLATION_API_RATE_LIMIT", "100"))
TTS_API_RATE_LIMIT = int(os.getenv("TTS_API_RATE_LIMIT", "50"))
RETRY_ATTEMPTS = int(os.getenv("RETRY_ATTEMPTS", "3"))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", "5"))

# ============================================================================
# MODEL CACHE SETTINGS
# ============================================================================

ENABLE_MODEL_CACHE = os.getenv("ENABLE_MODEL_CACHE", "True").lower() == "true"
MODEL_CACHE_DIR = CACHE_DIR / "models"
MODEL_CACHE_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================================
# QUALITY SETTINGS
# ============================================================================

MIN_LIP_CONFIDENCE = float(os.getenv("MIN_LIP_CONFIDENCE", "0.6"))
MAX_TIME_DRIFT = int(os.getenv("MAX_TIME_DRIFT", "100"))

QUALITY_PRESETS = {
    "low": {
        "video_crf": 28,
        "audio_bitrate": "128k",
        "max_resolution": (1280, 720),
    },
    "medium": {
        "video_crf": 23,
        "audio_bitrate": "192k",
        "max_resolution": (1920, 1080),
    },
    "high": {
        "video_crf": 18,
        "audio_bitrate": "320k",
        "max_resolution": (3840, 2160),
    },
}

DEFAULT_QUALITY = "medium"

# ============================================================================
# ADVANCED SETTINGS
# ============================================================================

NORMALIZE_AUDIO = os.getenv("NORMALIZE_AUDIO", "True").lower() == "true"
NORMALIZATION_TARGET_LOUDNESS = -20

REMOVE_SILENCE = os.getenv("REMOVE_SILENCE", "False").lower() == "true"
SILENCE_THRESHOLD = -40

PRESERVE_PAUSES = os.getenv("PRESERVE_PAUSES", "True").lower() == "true"

# ============================================================================
# FEATURE FLAGS
# ============================================================================

FEATURES = {
    "auto_subtitle_detection": True,
    "background_music_preservation": True,
    "emotion_voice_matching": False,
    "multilingual_mixing": False,
    "real_time_preview": False,
}

# ============================================================================
# ENVIRONMENT VALIDATION
# ============================================================================

def validate_config():
    """Validate configuration settings."""
    errors = []
    
    if not os.path.exists(GOOGLE_APPLICATION_CREDENTIALS):
        errors.append(
            f"Google Cloud credentials file not found: {GOOGLE_APPLICATION_CREDENTIALS}"
        )
    
    import shutil
    if not shutil.which(FFMPEG_PATH):
        errors.append(f"FFmpeg not found at: {FFMPEG_PATH}")
    
    if errors:
        print("Warning: Configuration issues found:")
        for error in errors:
            print(f"  - {error}")
    
    return len(errors) == 0

# ============================================================================
# CONFIGURATION DICTIONARY
# ============================================================================

CONFIG = {
    "project": {
        "name": PROJECT_NAME,
        "version": PROJECT_VERSION,
        "debug": DEBUG,
    },
    "google_cloud": {
        "project_id": GOOGLE_CLOUD_PROJECT_ID,
        "credentials": GOOGLE_APPLICATION_CREDENTIALS,
    },
    "translation": {
        "source_language": SOURCE_LANGUAGE,
        "target_language": TARGET_LANGUAGE,
        "supported_languages": SUPPORTED_LANGUAGES,
    },
    "tts": {
        "voices": TTS_VOICES,
        "rate": TTS_RATE,
        "pitch": TTS_PITCH,
        "volume": TTS_VOLUME,
    },
    "audio": {
        "sample_rate": AUDIO_SAMPLE_RATE,
        "channels": AUDIO_CHANNELS,
        "codec": AUDIO_CODEC,
        "bitrate": AUDIO_BITRATE,
    },
    "video": {
        "codec": VIDEO_CODEC,
        "preset": VIDEO_PRESET,
        "crf": VIDEO_CRF,
        "formats": VIDEO_FORMATS,
    },
    "performance": {
        "max_workers": MAX_WORKERS,
        "batch_size": BATCH_SIZE,
        "use_gpu": USE_GPU,
    },
    "paths": {
        "temp": str(TEMP_DIR),
        "output": str(OUTPUT_DIR),
        "cache": str(CACHE_DIR),
        "logs": str(LOGS_DIR),
    },
}

if __name__ == "__main__":
    separator = "=" * 60
    print("\n" + separator)
    print("DichPhim Configuration")
    print(separator + "\n")
    
    print(f"Project: {PROJECT_NAME} v{PROJECT_VERSION}")
    print(f"Debug Mode: {DEBUG}")
    print(f"\nLanguage: {SOURCE_LANGUAGE} -> {TARGET_LANGUAGE}")
    print(f"\nPaths:")
    print(f"  Temp: {TEMP_DIR}")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"  Cache: {CACHE_DIR}")
    print(f"  Logs: {LOGS_DIR}")
    print(f"\nPerformance:")
    print(f"  Workers: {MAX_WORKERS}")
    print(f"  GPU: {USE_GPU}")
    print(f"\nQuality Preset: {DEFAULT_QUALITY}")
    print("\n" + separator + "\n")
    
    if validate_config():
        print("Configuration is valid!\n")
    else:
        print("Please check the warnings above.\n")
