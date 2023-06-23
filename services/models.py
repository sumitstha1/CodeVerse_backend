from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

# Create your models here.
class Service(BaseModel):
    image = models.ImageField(upload_to="codeverse/service")
    banner_image = models.ImageField(upload_to="codeverse/service/banner")
    title = models.CharField(max_length=255)
    meta_description = models.TextField()
    description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
class Blog(BaseModel):
    image = models.ImageField(upload_to="codeverse/blog")
    title = models.CharField(max_length=255)
    introduction = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

class BlogSection(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="section")
    image = models.ImageField(upload_to="codeverse/blog", null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    