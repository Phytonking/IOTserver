from django.db import models
from web.models import *
# Create your models here.
class parent_folder(models.Model):
    folder_name=models.TextField()
    folder_owner=models.ForeignKey(u, on_delete=models.CASCADE, related_name="owner")
    #in_folder = models.ForeignKey(folder, on_delete=models.CASCADE, related_name="parent_folder", null=True)

class folder(models.Model):
    folder_name=models.TextField()
    folder_owner=models.ForeignKey(u, on_delete=models.CASCADE, related_name="user_owner")
    in_parent_folder = models.ForeignKey(parent_folder, on_delete=models.CASCADE, related_name="parent_folder", null=True)

class files(models.Model):
    file_name = models.TextField()
    file_owner = models.ForeignKey(u, on_delete=models.CASCADE, related_name="manager")
    file_size_bytes = models.BigIntegerField()
    in_folder = models.ForeignKey(folder, on_delete=models.CASCADE, related_name="folder", null=True)
    in_parent_folder = models.ForeignKey(parent_folder, on_delete=models.CASCADE, related_name="par_folder", null=True)


