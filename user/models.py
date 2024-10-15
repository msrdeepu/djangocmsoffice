from django.db import models


# Create your models here.
class Permission(models.Model):
    code = models.CharField(max_length=100, unique=True)  # Code/Name
    display_name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.display_name
    
    
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Code/Name
    display_name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    permissions = models.ManyToManyField('Permission', related_name='roles')  # Permissions (Many-to-Many)

    def __str__(self):
        return self.display_name
    
class Member(models.Model):
    WHATSAPP_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  # Link to Role model
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    phone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.CharField(max_length=3, choices=WHATSAPP_CHOICES, default='no')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.role.display_name})"