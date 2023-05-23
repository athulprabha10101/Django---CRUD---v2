from django.db import models

# Create your models here.
class custom_user(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

def __str__(self):
    return f"Username: {self.username}, First Name: {self.first_name}, Email: {self.email}"