# DichPhim - AI Movie Translator & Dubber

🎬 Phần mềm dịch và lồng tiếng phim tự động bằng AI, tương tự CapCut AI, HeyGen, Rask AI.

## ✨ Tính năng

- ✅ **Nhận diện giọng nói** tự động (Whisper)
- ✅ **Dịch đa ngôn ngữ** (GPT-4, Gemini, DeepL)
- ✅ **Tạo lồng tiếng** (Edge TTS, XTTS, Fish Speech)
- ✅ **Clone giọng** nhân vật (XTTS v2, F5-TTS)
- ✅ **Đồng bộ môi** (Wav2Lip, LatentSync)
- ✅ **Ghép video** tự động (FFmpeg)

## 🏗️ Kiến trúc

```
dichphim/
├── README.md
├── requirements.txt
├── config.py
├── app.py
├── .env.example
├── .gitignore
│
├── audio/              # Xử lý âm thanh
│   ├── __init__.py
│   ├── extract.py
│   ├── merge.py
│   └── normalize.py
│
├── stt/                # Speech-to-Text (Whisper)
│   ├── __init__.py
│   └── whisper_engine.py
│
├── translate/          # Dịch văn bản
│   ├── __init__.py
│   ├── gpt.py
│   ├── gemini.py
│   └── deepl.py
│
├── tts/                # Text-to-Speech
│   ├── __init__.py
│   ├── edge_tts.py
│   ├── xtts.py
│   └── fishspeech.py
│
├── subtitle/           # Xử lý phụ đề
│   ├── __init__.py
│   ├── srt.py
│   └── timing.py
│
├── video/              # Xử lý video
│   ├── __init__.py
│   └── ffmpeg_ops.py
│
├── lipsync/            # Lip Sync
│   ├── __init__.py
│   └── wav2lip.py
│
└── pipeline/           # Main processor
    ├── __init__.py
    └── processor.py
```

## 🚀 Cài đặt

### 1. Clone repository
```bash
git clone https://github.com/hpkchcn-netizen/dichphim.git
cd dichphim
```

### 2. Tạo virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Cài dependencies
```bash
pip install -r requirements.txt
```

### 4. Cài FFmpeg
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
choco install ffmpeg
```

### 5. Tạo file `.env`
```bash
cp .env.example .env
```

Sửa `.env` và thêm API keys:
```
OPENAI_API_KEY=your_key
GEMINI_API_KEY=your_key
DEEPL_API_KEY=your_key
```

## 💻 Sử dụng

### GUI Mode
```bash
python app.py
```

### CLI Mode
```bash
python -m pipeline.processor \
  --input movie.mp4 \
  --output movie_vi.mp4 \
  --source-lang en \
  --target-lang vi
```

## 🔧 Pipeline xử lý

1. **Tách âm thanh** → `audio.wav`
2. **STT (Whisper)** → segments với timestamp
3. **Dịch** → text tiếng Việt
4. **TTS** → audio tiếng Việt
5. **Time Stretch** → khớp duration
6. **Voice Clone** (tuỳ chọn) → nghe giống diễn viên
7. **Lip Sync** (tuỳ chọn) → miệng khớp tiếng
8. **Ghép Video** → output final

## 📦 Technologies

| Chức năng | Công nghệ |
|-----------|----------|
| Giao diện | CustomTkinter / Tkinter |
| Video | FFmpeg |
| STT | Whisper Large-v3 |
| Dịch | GPT-4 / Gemini / DeepL |
| TTS | Edge TTS / XTTS / Fish Speech |
| Clone | XTTS v2 / F5-TTS |
| Lip Sync | Wav2Lip / LatentSync |

## 📝 License

MIT License

## 👨‍💻 Author

[@hpkchcn-netizen](https://github.com/hpkchcn-netizen)