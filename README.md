# Dịch Phim (DichPhim) - Vietnamese Video Dubbing Tool

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/status-Alpha-yellow.svg)

## Overview

**Dịch Phim** is an automated Vietnamese video dubbing tool that combines:
- 🎬 **AI-powered translation** (Google Cloud Translate)
- 🔊 **Text-to-Speech** (Edge TTS)
- 📝 **Subtitle synchronization** (SRT/VTT support)
- 👄 **Lip-sync adjustment** (ML-based)
- 🎞️ **Video processing** (FFmpeg + OpenCV)

Automatic dubbing for international content into Vietnamese with lip-sync correction.

## Features

✨ **Core Features:**
- Auto-extract audio from videos
- Speech-to-text recognition
- AI translation (English → Vietnamese)
- Natural Vietnamese TTS synthesis
- SRT/VTT subtitle processing
- Lip-sync correction using ML
- Multi-format video support (MP4, MKV, AVI, etc.)
- Batch processing
- Progress tracking with tqdm

## Installation

### Prerequisites
- Python 3.8+
- FFmpeg installed on your system

```bash
# Clone the repository
git clone https://github.com/hpkchcn-netizen/dichphim.git
cd dichphim

# Install dependencies
pip install -r requirements.txt

# Or install as a package
pip install -e .
```

### FFmpeg Setup

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**MacOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## Quick Start

```python
from dichphim import VideoDubber

# Initialize
dubber = VideoDubber()

# Process a video
result = dubber.dub(
    input_video="movie.mp4",
    output_video="movie_vn.mp4",
    source_language="en",
    target_language="vi"
)

print(f"Dubbed video: {result['output_path']}")
```

## Project Structure

```
dichphim/
├── dichphim/
│   ├── __init__.py
│   ├── audio/
│   │   ├── extractor.py      # Audio extraction
│   │   ├── synthesizer.py    # TTS synthesis
│   │   └── merger.py         # Audio merging
│   ├── subtitle/
│   │   ├── parser.py         # SRT/VTT parsing
│   │   ├── translator.py     # Translation service
│   │   └── synchronizer.py   # Sync adjustment
│   ├── video/
│   │   ├── processor.py      # Video processing
│   │   ├── detector.py       # Face/lip detection
│   │   └── renderer.py       # Video rendering
│   ├── ml/
│   │   ├── lipsync.py        # Lip-sync model
│   │   └── alignment.py      # Speech alignment
│   └── core.py               # Main dubber class
├── tests/
├── examples/
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE
```

## Configuration

Create a `.env` file in the project root:

```env
# Google Cloud Translation
GOOGLE_CLOUD_PROJECT_ID=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json

# Optional settings
MAX_WORKERS=4
DEBUG=False
```

## API Reference

### VideoDubber

```python
class VideoDubber:
    def dub(
        self,
        input_video: str,
        output_video: str,
        source_language: str = "en",
        target_language: str = "vi",
        subtitle_file: Optional[str] = None,
        enable_lipsync: bool = True,
        output_format: str = "mp4"
    ) -> Dict[str, Any]
```

## Examples

See the `examples/` directory for:
- Basic video dubbing
- Batch processing
- Subtitle-only translation
- Custom TTS voices

## Development

### Setup Development Environment

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Code formatting
black dichphim/

# Linting
flake8 dichphim/

# Type checking
mypy dichphim/
```

## Performance

- **Video processing:** ~2-5x realtime (depends on resolution)
- **Translation:** ~500 words/minute
- **TTS:** ~100-200 words/minute
- **Lip-sync:** ~5-10x realtime

## Limitations

⚠️ **Current Alpha Limitations:**
- Works best with clear audio and frontal face angles
- Lip-sync accuracy varies by video quality
- Limited language support (English → Vietnamese)
- Subtitle file required for best results

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Troubleshooting

### Common Issues

**FFmpeg not found:**
```bash
# Add FFmpeg to PATH or specify location
export FFMPEG_PATH=/path/to/ffmpeg
```

**Google Cloud authentication error:**
```bash
# Ensure credentials are set
export GOOGLE_APPLICATION_CREDENTIALS=path/to/key.json
```

## Roadmap

- [ ] Support for more languages
- [ ] Improved lip-sync accuracy
- [ ] GPU acceleration
- [ ] Web UI
- [ ] Cloud API service

## License

MIT License - see [LICENSE](LICENSE) file

## Author

**hpkchcn-netizen**
- GitHub: [@hpkchcn-netizen](https://github.com/hpkchcn-netizen)
- Email: hpkchcn@gmail.com

## Acknowledgments

- Google Cloud Translation API
- Edge TTS library
- FFmpeg community
- OpenCV project

## Support

For issues and questions:
- 🐛 [Bug Reports](https://github.com/hpkchcn-netizen/dichphim/issues)
- 💬 [Discussions](https://github.com/hpkchcn-netizen/dichphim/discussions)
- 📧 Email: hpkchcn@gmail.com

---

**Made with ❤️ for Vietnamese content creators**