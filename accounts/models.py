from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

# Create your models here.
class Profile(BaseModel):
    logo = models.ImageField(upload_to="codeverse/profile")
    name = models.CharField(max_length=255)
    description = models.TextField()
    why_codeverse = models.TextField()
    email = models.EmailField()
    contact = models.CharField(max_length=255)
    contact2 = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Profile, self).save(*args, **kwargs)

class SocialHandles(BaseModel):
    name = models.CharField(max_length=255)
    url = models.URLField()

class Newsletter(BaseModel):
    email = models.EmailField(unique=True)

