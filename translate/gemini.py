"""Google Gemini Translation"""

import google.generativeai as genai
from typing import List, Optional
import logging
import os

logger = logging.getLogger(__name__)


class GeminiTranslator:
    """Google Gemini Translation Engine"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Gemini translator

        Args:
            api_key: Google Gemini API key (uses env var if None)
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def translate(
        self,
        text: str,
        source_lang: str = "English",
        target_lang: str = "Vietnamese",
    ) -> str:
        """
        Translate text using Gemini

        Args:
            text: Text to translate
            source_lang: Source language name
            target_lang: Target language name

        Returns:
            Translated text
        """
        logger.info(f"Translating {len(text)} chars ({source_lang} -> {target_lang})...")

        prompt = f"""Translate the following {source_lang} text to {target_lang}.
Keep the original meaning and tone.
Translate ONLY the text, no explanations.

Text to translate:
{text}

Translation:"""

        try:
            response = self.model.generate_content(prompt)
            translated = response.text.strip()
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
            target_lang: Target language name

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