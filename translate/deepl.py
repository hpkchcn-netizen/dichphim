"""DeepL Translation"""

import deepl
from typing import List, Optional
import logging
import os

logger = logging.getLogger(__name__)


class DeepLTranslator:
    """DeepL Translation Engine"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize DeepL translator

        Args:
            api_key: DeepL API key (uses env var if None)
        """
        self.api_key = api_key or os.getenv("DEEPL_API_KEY")
        if not self.api_key:
            raise ValueError("DEEPL_API_KEY not found in environment")

        self.translator = deepl.Translator(self.api_key)

    def translate(
        self,
        text: str,
        source_lang: str = "EN",
        target_lang: str = "VI",
    ) -> str:
        """
        Translate text using DeepL

        Args:
            text: Text to translate
            source_lang: Source language code (EN, ZH, JA, etc.)
            target_lang: Target language code

        Returns:
            Translated text
        """
        logger.info(f"Translating {len(text)} chars ({source_lang} -> {target_lang})...")

        try:
            result = self.translator.translate_text(
                text,
                source_lang=source_lang,
                target_lang=target_lang,
            )
            translated = result.text
            logger.info(f"✅ Translation complete")
            return translated
        except Exception as e:
            logger.error(f"Translation failed: {e}")
            raise

    def translate_segments(self, segments: List[dict], target_lang: str) -> List[dict]:
        """
        Translate subtitle segments

        Args:
            segments: List of subtitle segments
            target_lang: Target language code

        Returns:
            Segments with 'translated_text' field added
        """
        for i, segment in enumerate(segments):
            segment["translated_text"] = self.translate(
                segment["text"],
                target_lang=target_lang,
            )
            logger.info(f"  [{i+1}/{len(segments)}] {segment['text'][:50]}...")

        return segments