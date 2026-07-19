"""GPT-based Translation"""

import openai
from typing import List, Optional
import logging
import os

logger = logging.getLogger(__name__)


class GPTTranslator:
    """OpenAI GPT Translation Engine"""

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        """
        Initialize GPT translator

        Args:
            api_key: OpenAI API key (uses env var if None)
            model: GPT model to use (gpt-4, gpt-3.5-turbo)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        self.client = openai.OpenAI(api_key=self.api_key)

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")

    def translate(
        self,
        text: str,
        source_lang: str = "English",
        target_lang: str = "Vietnamese",
        context: Optional[str] = None,
    ) -> str:
        """
        Translate text using GPT

        Args:
            text: Text to translate
            source_lang: Source language name
            target_lang: Target language name
            context: Additional context for translation

        Returns:
            Translated text
        """
        logger.info(f"Translating {len(text)} chars from {source_lang} to {target_lang}...")

        prompt = f"""Translate the following {source_lang} text to {target_lang}.
Keep the original meaning and tone.
Translate ONLY the text, no explanations.

{f"Context: {context}" if context else ""}

Text to translate:
{text}

Translation:"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
            )
            translated = response.choices[0].message.content.strip()
            logger.info(f"✅ Translation complete")
            return translated
        except Exception as e:
            logger.error(f"Translation failed: {e}")
            raise

    def translate_segments(self, segments: List[dict], target_lang: str) -> List[dict]:
        """
        Translate subtitle segments

        Args:
            segments: List of subtitle segments {id, start, end, text}
            target_lang: Target language name

        Returns:
            Same segments with 'translated_text' field added
        """
        for i, segment in enumerate(segments):
            segment["translated_text"] = self.translate(
                segment["text"],
                target_lang=target_lang,
            )
            logger.info(f"  [{i+1}/{len(segments)}] {segment['text'][:50]}...")

        return segments