from django.db import models
from web.models import *
# Create your models here.
class files(models.Model):
    file_name = models.TextField()
    file_owner = models.ForeignKey(u, on_delete=models.CASCADE, related_name="owner")
    file_size_bytes = models.BigIntegerField()
    in_folder = models.TextField(null=True)
