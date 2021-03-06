from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(blank=True, upload_to='pics', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
