from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

translator = Translator()

LANGUAGES = ['hi', 'bn']  # Add more languages as needed

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Translated fields
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Automatically translate the question and answer."""
        for lang in LANGUAGES:
            cache_key = f"faq_translation_{self.pk}_{lang}"
            cached_translation = cache.get(cache_key)

            if not cached_translation:
                setattr(self, f'question_{lang}', translator.translate(self.question, dest=lang).text)
                setattr(self, f'answer_{lang}', translator.translate(self.answer, dest=lang).text)
                cache.set(cache_key, (self.question, self.answer), timeout=86400)

        super().save(*args, **kwargs)

    def get_translation(self, lang):
        """Retrieve the translated question and answer."""
        if lang in LANGUAGES:
            return {
                "question": getattr(self, f'question_{lang}', self.question),
                "answer": getattr(self, f'answer_{lang}', self.answer)
            }
        return {"question": self.question, "answer": self.answer}

    def __str__(self):
        return self.question
