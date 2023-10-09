from django.db import models
from core.sorting import sort_files_path


class File(models.Model):
    file = models.FileField(
        upload_to=sort_files_path
    )
    upload_at = models.DateTimeField(
        auto_now_add=True
    )
    processed = models.BooleanField(
        default=False
    )
