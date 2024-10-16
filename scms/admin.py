from django.contrib import admin
from .models import Page


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published_on', 'published', 'page_type', 'link_text')  # Correct this line
    list_filter = ('published', 'page_type')
    search_fields = ('title', 'slug', 'navigation_text', 'page_title')

    fieldsets = (
        ('Meta Information', {
            'fields': ('title', 'slug', 'navigation_text', 'page_title', 'meta_description', 'meta_keywords')
        }),
        ('Content Section', {
            'fields': ('main_header', 'sub_header', 'page_type', 'link_text','enable_gallery', 'enable_uploads', 'body1', 'body2', 'body3', 'body4', 'extra_body', 'rich_intro', 'rich_body')
        }),
        ('Call to Action', {
            'fields': ('cta_header', 'cta_body', 'cta_action_text', 'cta_link_url')
        }),
        ('Attachments', {
            'fields': ('thumbnail', 'image', 'banner')
        }),
        ('Settings', {
            'fields': ('published_on', 'published', 'expires_on', 'content_access_level')
        }),
    )
    
    ordering = ('published_on',)
    
admin.site.register(Page, PageAdmin)