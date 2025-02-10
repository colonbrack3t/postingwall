from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class MyImageModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/images',null=True, blank=True)
    video = models.FileField(upload_to='uploads/videos/', blank=True, null=True)
    text = CKEditor5Field(null=True, blank=True)
    publish = models.BooleanField(default=False)
    author = models.CharField(max_length=2047)
    def __str__(self):
        if self.image:
            return self.image.url
        elif self.video:
            return self.video.name
        else:
            return self.text.__str__()[:10]


class SiteInfo(models.Model):
    title = models.CharField(max_length=120)
    icon = models.ImageField(upload_to='uploads/icon',null=True, blank=True)
    headertext=CKEditor5Field('Text', config_name='extends',null=True, blank=True)
