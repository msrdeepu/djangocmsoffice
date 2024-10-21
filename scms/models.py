from django.db import models
from django.db import models
from django.utils.text import slugify
from setup.models import Category, SelectList

# Create your models here.


class Page(models.Model):
    # === Meta Section ===
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    navigation_text = models.CharField(max_length=255)
    page_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    # === Content Section ===
    
    main_header = models.CharField(max_length=255)
    sub_header = models.CharField(max_length=255, blank=True)
    enable_gallery = models.BooleanField(default=False)  
    enable_uploads = models.BooleanField(default=False)
  
    
    # Page Type dropdown (loading from SelectList model)
    page_type = models.CharField(max_length=50, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='PAGETYPE')])
    link_text = models.CharField(max_length=255, blank=True, null=True)

    # Conditional fields based on Page Type
    extra_body = models.TextField(blank=True, null=True)
    rich_intro = models.TextField(blank=True, null=True)
    rich_body = models.TextField(blank=True, null=True)
    teaser = models.TextField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    main_body = models.TextField(blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)
    body4 = models.TextField(blank=True, null=True)


    # === Attachments ===
    thumb = models.ImageField(upload_to='uploads/thumbs/', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    banner = models.ImageField(upload_to='uploads/banners/', blank=True, null=True)

    # SEO Attachments
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    seo_banner = models.ImageField(upload_to='uploads/seo_banners/', blank=True, null=True)
    attachment1 = models.ImageField(upload_to='uploads/attachments/', blank=True, null=True)
    attachment2 = models.ImageField(upload_to='uploads/attachments/', blank=True, null=True)

    # === Call to Action ===
    cta_header = models.CharField(max_length=255, blank=True, null=True)
    cta_body = models.TextField(blank=True, null=True)
    cta_action_text = models.CharField(max_length=255, blank=True, null=True)
    cta_link_url = models.URLField(blank=True, null=True)

    # === Settings Section ===
    category = models.CharField(max_length=255, choices=[(cat.name, cat.name) for cat in Category.objects.all()])
    group = models.CharField(max_length=50, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='GROUP')])
    page_layout = models.CharField(max_length=50, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='LAYOUT')])

    # === Publish Section ===
    published_on = models.DateField()
    published = models.BooleanField(default=False)
    expires_on = models.DateField(null=True, blank=True)
    content_access_level = models.CharField(max_length=50, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='CONTENTACCESS')])

    # Auto slugify the title if slug is not provided
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        
        