# users/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
    	User, 
    	on_delete=models.CASCADE, 
    	null=True, blank=True)
    name = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True)
    email = models.EmailField(
    	max_length=500, 
    	blank=True, 
    	null=True)
    username = models.CharField(
        max_length=200, 
        blank=True, 
        null=True)
    location = models.CharField(
        max_length=200, 
        blank=True, 
        null=True)
    short_intro = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True)
    bio = models.TextField(
    	blank=True, 
    	null=True)
    profile_image = models.ImageField(
    	null=True, 
    	blank=True, 
    	upload_to='profiles/', 
    	default="profiles/user-default.png")
    social_github = models.CharField(
    	max_length=200, 
    	blank=True, null=True)
    social_twitter = models.CharField(
    	max_length=200, 
    	blank=True, null=True)
    social_linkedin = models.CharField(
    	max_length=200, 
    	blank=True, null=True)
    social_youtube = models.CharField(
    	max_length=200, 
    	blank=True, null=True)
    social_website = models.CharField(
    	max_length=200, 
    	blank=True, null=True)
    created = models.DateTimeField(
    	auto_now_add=True)
    id = models.UUIDField(
    	default=uuid.uuid4, 
	    unique=True,
	    primary_key=True, 
	    editable=False)

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    '''
    Membuat hubungan OneToMany antar Profile dan Skill.
    Profile, dalam hal ini seorang owner dapat memiliki
    0, 1 atau banyak skill. Atau setiap skill dimiliki
    oleh seorang owner.
    '''
    owner = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True)
    name = models.CharField(
        max_length=200, 
        blank=True, 
        null=True)
    description = models.TextField(
        null=True, 
        blank=True)
    created = models.DateTimeField(
        auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True, 
        primary_key=True, 
        editable=False)

    def __str__(self):
        return str(self.name)


# # Singnals
# def profileUpdate(sender, instance, created, **kwargs):
#     print('PROFILE saved!')
#     print('Instance:', instance)
#     print('CREATED:', created)

# def deleteUser(sender, instance, **kwargs):
#     print('DELETING user ...')

# post_save.connect(profileUpdate, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)


# Decorator
@receiver(post_save, sender=Profile)
def profileUpdate(sender, instance, created, **kwargs):
    print('PROFILE saved!')
    print('Instance:', instance)
    print('CREATED:', created)

'''Anytime delete a profile, it aslo delete the user'''
@receiver(post_save, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    print('DELETING user ...')