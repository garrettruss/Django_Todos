from django.db import models

# Create your models here.

class Todo(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.description