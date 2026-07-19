"""Command-line interface for dichphim"""

import argparse
import logging
import sys
from pathlib import Path

from pipeline.orchestrator import DubPipeline

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def create_parser():
    """
    Create argument parser for CLI

    Returns:
        ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        description="dichphim - Vietnamese Video Dubbing Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic dubbing
  dichphim dub -v video.mp4 -s subtitles.srt
  
  # With custom output
  dichphim dub -v video.mp4 -s subtitles.srt -o dubbed.srt
  
  # With custom voice
  dichphim dub -v video.mp4 -s subtitles.srt --voice en-GB-SoniaNeural
  
  # Show help
  dichphim --help
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Dub command
    dub_parser = subparsers.add_parser("dub", help="Dub a video")
    dub_parser.add_argument(
        "-v",
        "--video",
        required=True,
        type=str,
        help="Input video file",
    )
    dub_parser.add_argument(
        "-s",
        "--subtitles",
        required=True,
        type=str,
        help="Input subtitle file (SRT format)",
    )
    dub_parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="dubbed_output.srt",
        help="Output subtitle file (default: dubbed_output.srt)",
    )
    dub_parser.add_argument(
        "--source-lang",
        type=str,
        default="vi",
        help="Source language code (default: vi)",
    )
    dub_parser.add_argument(
        "--target-lang",
        type=str,
        default="en",
        help="Target language code (default: en)",
    )
    dub_parser.add_argument(
        "--voice",
        type=str,
        default="en-US-AriaNeural",
        help="TTS voice to use (default: en-US-AriaNeural)",
    )
    dub_parser.add_argument(
        "--temp-dir",
        type=str,
        default="./temp",
        help="Temporary directory for audio files (default: ./temp)",
    )
    dub_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    # Version command
    subparsers.add_parser("version", help="Show version information")

    return parser


def cmd_dub(args):
    """
    Handle dub command

    Args:
        args: Parsed arguments
    """
    # Validate input files
    video_file = Path(args.video)
    srt_file = Path(args.subtitles)

    if not video_file.exists():
        logger.error(f"Video file not found: {video_file}")
        sys.exit(1)

    if not srt_file.exists():
        logger.error(f"Subtitle file not found: {srt_file}")
        sys.exit(1)

    try:
        # Create pipeline
        logger.info(f"🎬 Dubbing {video_file.name}")
        logger.info(f"📝 Subtitles: {srt_file.name}")
        logger.info(f"🗣️  Voice: {args.voice}")
        logger.info(f"📂 Output: {args.output}")

        pipeline = DubPipeline(
            source_lang=args.source_lang,
            target_lang=args.target_lang,
            voice=args.voice,
        )

        # Run pipeline
        result = pipeline.run(
            video_file=str(video_file),
            srt_file=str(srt_file),
            output_srt=args.output,
            temp_dir=args.temp_dir,
        )

        logger.info(f"\n✅ Success!")
        logger.info(f"Output: {result['output_srt']}")
        logger.info(f"Audio files: {result['audio_dir']}")
        logger.info(f"Segments: {result['segments_count']}")

    except Exception as e:
        logger.error(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


def cmd_version(args):
    """
    Handle version command

    Args:
        args: Parsed arguments
    """
    version = "0.1.0"
    print(f"dichphim v{version}")
    print("Vietnamese Video Dubbing Tool")
    print("https://github.com/hpkchcn-netizen/dichphim")


def main():
    """
    Main CLI entry point
    """
    parser = create_parser()
    args = parser.parse_args()

    # If no command provided, show help
    if not args.command:
        parser.print_help()
        sys.exit(0)

    # Route to command handler
    if args.command == "dub":
        cmd_dub(args)
    elif args.command == "version":
        cmd_version(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()