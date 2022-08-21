from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class ManifestModel(models.Model):
    goal = models.CharField(max_length=64)
    description = models.TextField(default="")
    image_url = models.URLField(default="https://images.unsplash.com/photo-1609517269751-3c8de889ce97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80")
    dreamer = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    def __str__(self):
        return self.goal

    def get_absolute_url(self):
        return reverse('detail_manifestation', args=[str(self.id)])

    

