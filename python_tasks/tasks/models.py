from django.db import models
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    LEVEL_CHOICES = [
        ('beginner', _('Начинающий')),
        ('intermediate', _('Средний')),
        ('advanced', _('Продвинутый')),
    ]

    title_ru = models.CharField(max_length=200, default='')
    title_en = models.CharField(max_length=200, default='')

    description_ru = models.TextField(default='')
    description_en = models.TextField(default='')

    answer_code = models.TextField(default='')

    explanation_ru = models.TextField(default='')
    explanation_en = models.TextField(default='')

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.title_ru or self.title_en or f"Задача #{self.pk}"

    def get_title(self, lang):
        return self.title_en if lang == 'en' else self.title_ru

    def get_description(self, lang):
        return self.description_en if lang == 'en' else self.description_ru

    def get_explanation(self, lang):
        return self.explanation_en if lang == 'en' else self.explanation_ru
