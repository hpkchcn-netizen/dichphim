"""Configuration for DichPhim AI Movie Translator"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Paths
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "./output"))
TEMP_DIR = Path(os.getenv("TEMP_DIR", "./temp"))
MODELS_DIR = BASE_DIR / "models"

# Create directories
OUTPUT_DIR.mkdir(exist_ok=True)
TEMP_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

# Language settings
DEFAULT_SOURCE_LANG = os.getenv("DEFAULT_SOURCE_LANG", "en")
DEFAULT_TARGET_LANG = os.getenv("DEFAULT_TARGET_LANG", "vi")

SUPPORTED_LANGUAGES = {
    "en": "English",
    "vi": "Tiếng Việt",
    "zh": "中文",
    "ja": "日本語",
    "ko": "한국어",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "ru": "Русский",
    "pt": "Português",
}

# Whisper STT settings
WHISPER_MODEL_SIZE = os.getenv("WHISPER_MODEL_SIZE", "large")
WHISPER_MODELS = ["tiny", "base", "small", "medium", "large"]
WHISPER_DEVICE = "cuda"
WHISPER_COMPUTE_TYPE = "float16"

# Translation settings
TRANSLATION_SERVICE = "gpt"

# TTS settings
TTS_ENGINE = os.getenv("TTS_ENGINE", "edge")
TTS_ENGINES = ["edge", "xtts", "fish"]
EDGE_TTS_VOICE = "vi-VN-HoaiMyNeural"
XTTS_SAMPLE_RATE = 22050

# Voice cloning
ENABLE_VOICE_CLONE = os.getenv("ENABLE_VOICE_CLONE", "true").lower() == "true"
VOICE_CLONE_ENGINE = "xtts"

# Lip sync
ENABLE_LIP_SYNC = os.getenv("ENABLE_LIP_SYNC", "true").lower() == "true"
LIP_SYNC_ENGINE = "wav2lip"

# Time stretch
ENABLE_TIME_STRETCH = os.getenv("ENABLE_TIME_STRETCH", "true").lower() == "true"

# FFmpeg settings
FFMPEG_PATH = os.getenv("FFMPEG_PATH", "ffmpeg")
FFMPEG_AUDIO_CODEC = "aac"
FFMPEG_VIDEO_CODEC = "h264"
FFMPEG_QUALITY = "high"

# Processing settings
BATCH_SIZE = 4
MAX_WORKERS = 4

# Audio settings
AUDIO_SAMPLE_RATE = 16000
AUDIO_CHANNELS = 1

print("✅ Config loaded successfully")