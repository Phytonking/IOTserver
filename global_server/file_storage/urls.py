from django.urls import path
from file_storage.views import *
app_name="files"

urlpatterns = [
    path("list", list_files, name="list_files"),
    #path("add", add_file, name="add_file"),
    #path("delete", delete_file, name="delete_file")
    #path("update", update_file, name="update_file")
]