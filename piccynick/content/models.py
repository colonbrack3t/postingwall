from django.db import models

class MyImageModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/images',null=True, blank=True)
    video = models.FileField(upload_to='uploads/videos/', blank=True, null=True)
    text = models.TextField(null=True, blank=True)
    def __str__(self):
        if self.image:
            return self.image.url
        elif self.video:
            return self.video.name
        else:
            return self.text.__str__()[:10]
