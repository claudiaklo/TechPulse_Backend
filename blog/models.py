from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    color = models.CharField(max_length=20, help_text="Hex color code (e.g., #6366f1)")
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class (e.g., bi-code-square)")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.URLField(help_text="URL to avatar image")
    bio = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField()
    content = models.TextField(help_text="Markdown content")
    cover_image = models.URLField(help_text="URL to cover image", blank=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True, help_text="Upload cover image (overrides cover_image URL)")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    tags = models.JSONField(default=list, help_text="List of tags")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    published_at = models.DateTimeField()
    reading_time = models.IntegerField(help_text="Estimated reading time in minutes")
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # If an image is uploaded, clear the external URL to avoid ambiguity
        if self.image:
            self.cover_image = ''
            
        super().save(*args, **kwargs)
