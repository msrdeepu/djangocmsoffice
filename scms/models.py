from django.db import models

# Create your models here.
class Member(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('partner', 'Partner'),
        ('agent', 'Agent'),
        ('client', 'Client'),
    ]

    WHATSAPP_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    phone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.BooleanField(choices=WHATSAPP_CHOICES, default=False)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    password = models.CharField(max_length=128)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.role}"
    

