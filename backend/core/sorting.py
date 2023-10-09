import os
from django.conf import settings


def sort_files_path(instance, filename):
    _, extension = os.path.splitext(filename)
    file_type = 'other'
    if extension.lower() in ('.jpg', '.jpeg'):
        file_type = 'image'
    elif extension.lower() in ('.pdf', '.doc', '.docx'):
        file_type = 'document'
    return os.path.join(settings.MEDIA_ROOT, file_type, filename)
