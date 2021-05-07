from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.description