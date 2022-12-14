import io

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.fields.files import ImageFieldFile
 
 
class PhotoFieldFile(ImageFieldFile):
 
    def save(self, name, content, save=True):
        content.file.seek(0)
        image = Image.open(content.file)
        if image.format == "JPEG" or image.format == "PNG":
            image_bytes = io.BytesIO()
            image.save(fp=image_bytes, format="WEBP")
            image_content_file = ContentFile(content=image_bytes.getvalue())
            super().save(name, image_content_file, save)
        image_bytes = io.BytesIO()
        image.save(fp=image_bytes, format=image.format)
        image_content_file = ContentFile(content=image_bytes.getvalue())
        super().save(name, image_content_file, save)
 
 
class PhotoField(models.ImageField):
    attr_class = PhotoFieldFile