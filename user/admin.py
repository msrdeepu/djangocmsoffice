from django.contrib import admin
from .models import Permission, Role, Member

# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('code', 'display_name', 'description')
    search_fields = ('code', 'display_name')
    

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name', 'description')  
    search_fields = ('name', 'display_name')
    filter_horizontal = ('permissions',) 
    
class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'role', 'email', 'city', 'country')
    search_fields = ('firstname', 'lastname', 'email')
    list_filter = ('role', 'country')


admin.site.register(Permission, PermissionAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Member, MemberAdmin)
