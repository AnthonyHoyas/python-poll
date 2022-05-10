from distutils.command.upload import upload
from django.db import models

from BeTogether_backend.settings import AUTH_USER_MODEL

# Create your models here.
'''
groupe_project :
    Name
    Final_deadline

vote_list:
    Wishlist

Learner_project:
    name
    description
    databe_schema_picture
    mockup_picture

groups


'''

class Learner_project(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField
    database_schema_picture = models.ImageField(upload_to="images", blank=True, null=True)
    mockup_picture = models.ImageField(upload_to="images", blank=True, null=True)