from django.contrib.auth.models import User
from django.db import models


class HitCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    path = models.CharField(max_length=512)
    hits = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.path} ({self.hits})'

    def save(self, *args, **kwargs):
        print(self)
        return super().save(*args, **kwargs)
