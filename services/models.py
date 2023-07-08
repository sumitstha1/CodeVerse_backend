from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Service(BaseModel):
    image = models.URLField()
    banner_image = models.URLField()
    title = models.CharField(max_length=255)
    title_quote = models.CharField(max_length=500, null=True)
    meta_description = models.TextField()
    description = RichTextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    order = models.IntegerField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
class ServiceMetaTags(BaseModel):
    service = models.OneToOneField(Service, related_name="meta", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    
class Blog(BaseModel):
    image = models.URLField()
    title = models.CharField(max_length=500)
    introduction = RichTextField()
    meta_intro = models.TextField(null=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=500)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

class BlogSection(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="section")
    image = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = RichTextField()
    order = models.IntegerField(unique=True, null=True)

    def __str__(self) -> str:
        return self.blog.title

class BlogMetaTags(BaseModel):
    blog = models.OneToOneField(Blog, related_name="meta", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    