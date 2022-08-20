from django.db import models
from django.contrib.auth import get_user_model


class ManifestModel(models.Model):
    goal = models.CharField(max_length=64)
    description = models.TextField(default="")
    dreamer = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    def __str__(self):
        return self.goal

