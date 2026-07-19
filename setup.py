"""Setup configuration for dichphim"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dichphim",
    version="0.1.0",
    author="hpkchcn-netizen",
    author_email="hpkchcn@gmail.com",
    description="Vietnamese Video Dubbing Tool - Auto-dub videos with AI translation and TTS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hpkchcn-netizen/dichphim",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "google-cloud-translate>=3.11.1",
        "edge-tts>=6.1.1",
        "pydub>=0.25.1",
        "chardet>=5.2.0",
        "ffmpeg-python>=0.2.1",
        "opencv-python>=4.8.1.78",
        "scipy>=1.11.3",
        "numpy>=1.24.3",
        "scikit-learn>=1.3.2",
        "colorama>=0.4.6",
        "tqdm>=4.66.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "black>=23.11.0",
            "flake8>=6.1.0",
            "mypy>=1.7.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dichphim=cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)