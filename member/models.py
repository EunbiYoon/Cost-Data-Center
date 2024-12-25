from django.db import models

# Create your models here.
class User(models.Model):
    def __str__(self):
        return self.User
    class Meta:
        verbose_name_plural='User'