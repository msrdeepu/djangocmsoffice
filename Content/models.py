from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from setup.models import Category, SelectList

# Create your models here.
class SelectList(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    navigation_text = models.CharField(max_length=255)
    page_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    # Headers
    main_header = models.CharField(max_length=255)
    sub_header = models.CharField(max_length=255, blank=True)

    # Page Section Details
    page_type = models.ForeignKey('SelectList', on_delete=models.SET_NULL, null=True, related_name='content')
    link_text = models.CharField(max_length=255, blank=True)
    extra_body = models.TextField(blank=True)
    rich_intro = models.TextField(blank=True)
    rich_body = models.TextField(blank=True)

    # Call to Action (CTA) Fields
    cta_header = models.CharField(max_length=255, blank=True)
    cta_body = models.TextField(blank=True)
    cta_action_text = models.CharField(max_length=255, blank=True)
    cta_link_url = models.URLField(blank=True)

    # Page Settings
    published_on = models.DateField()
    published = models.BooleanField(default=False)
    expires_on = models.DateField(null=True, blank=True)
    content_access_level = models.ForeignKey('SelectList', on_delete=models.SET_NULL, null=True, related_name='content')

    # Attachments
    thumbnail = models.ImageField(upload_to='content/thumbnails/', blank=True, null=True)
    image = models.ImageField(upload_to='content/images/', blank=True, null=True)
    banner = models.ImageField(upload_to='content/banners/', blank=True, null=True)

    def __str__(self):
        return self.title

    # Override the save method to add slug logic
    def save(self, *args, **kwargs):
        # If slug is not manually entered, generate slug from title
        if not self.slug:
            self.slug = slugify(self.title)

        # Apply additional conditions to the slug or content fields based on certain rules
        if self.published_on and self.published and not self.expires_on:
            # Example condition: If content is published and does not have an expiry date,
            # modify the slug or add some special logic
            self.slug += "-active"
        
        # Ensure slug uniqueness
        if Content.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            raise ValidationError("Slug must be unique. This slug already exists.")
        
        super().save(*args, **kwargs)