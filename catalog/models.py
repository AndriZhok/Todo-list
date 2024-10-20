from django.utils import timezone

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    optional_deadline = models.DateTimeField(blank=True, null=True)
    if_field = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
