from django.db import models
from .actor import Actor


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True)
    year = models.IntegerField()
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
