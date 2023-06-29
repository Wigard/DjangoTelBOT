from django.db import models

# Create your models here.
class autoMessageItem(models.Model):
  command = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  url = models.CharField(max_length=255)
