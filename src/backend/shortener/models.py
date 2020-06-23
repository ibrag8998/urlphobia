from random import sample

from django.db import models
from django.shortcuts import reverse


class URL(models.Model):
    slug = models.SlugField(max_length=10, unique=True, db_index=True)
    destination = models.URLField()

    def save(self, *args, **kwargs):
        while True:
            try:
                self.slug = SlugGeneratorService.get_slug_suggestion()
            except Exception as e:
                print(e)
            else:
                break

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("shortener:info", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.slug} --> {self.destination}"


class SlugGeneratorService:
    symbols = ('QWERTYUIOPASDFGHJKLZXCVBNM'
               'qwertyuiopasdfghjklzxcvbnm'
               '1234567890-_')
    length = 7

    @classmethod
    def get_slug_suggestion(cls):
        """ Generate random slug for URL model """
        return ''.join(sample(cls.symbols, cls.length))
