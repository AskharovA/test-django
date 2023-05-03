from django.db import models
from django.utils.text import slugify


class ZodiacModel(models.Model):
    name = models.CharField(max_length=10)
    image = models.CharField(max_length=20)
    text = models.TextField()
    slug = models.SlugField(default='', null=False, db_index=True)
    harakter = models.TextField(default='', blank=True)
    sides = models.TextField(default='', blank=True)
    sovmestimost = models.TextField(default='', blank=True)