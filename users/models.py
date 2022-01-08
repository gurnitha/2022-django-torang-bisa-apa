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


# Step 1: Signals
#---------------------

# # Singnals
# def profileUpdate(sender, instance, created, **kwargs):
#     print('PROFILE saved!')
#     print('Instance:', instance)
#     print('CREATED:', created)

# def deleteUser(sender, instance, **kwargs):
#     print('DELETING user ...')

# post_save.connect(profileUpdate, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)


# # Step 2: Receiver and Signals
# #-----------------------------

# # Decorator
# @receiver(post_save, sender=Profile)
# def profileUpdate(sender, instance, created, **kwargs):
#     print('PROFILE saved!')
#     print('Instance:', instance)
#     print('CREATED:', created)

# '''Anytime delete a profile, it aslo delete the user'''
# @receiver(post_save, sender=Profile)
# def deleteUser(sender, instance, **kwargs):
#     print('DELETING user ...')


# # Step 3: Real live using Signals
# # Create a new user --> a new user's profile will 
# # also be created automatically

# # NOTE:
# # 1. User dibuat, profile terbuat
# # 2. User dihapus, profile terhapus
# # 3. Profile dihapus, user tidak terhapus
# #------------------------------------------------

# # Signals
# def createProfile(sender, instance, created, **kwargs):
#     # Check if this was the first signal of new user
#     if created:
#         user = instance # <-- instance of the User
#         new_user = user # <-- user = new_user
#         # If so, then create profile
#         profile = Profile.objects.create(
#             # Use the user to create
#             user = new_user,
#             # Create username, email, first_name
#             username = new_user.username,
#             email = new_user.email,
#             name = new_user.first_name 
#         )


# '''Anytime delete a profile, it aslo delete the user'''
# def deleteUser(sender, instance, **kwargs):
#     print('DELETING user ...')

# post_save.connect(createProfile, sender=User)
# post_delete.connect(deleteUser, sender=Profile)


# Step 4: Real live using Signals
# Create a new user --> a new user's profile will 
# also be created automatically

# NOTE:
# 1. User dibuat, profile terbuat
# 2. User dihapus, profile terhapus
# 3. Profile dihapus, user juga terhapus
#------------------------------------------------

# Signals
def createProfile(sender, instance, created, **kwargs):
    # Check if this was the first signal of new user
    if created:
        user = instance # <-- instance of the User
        new_user = user # <-- user = new_user
        # If so, then create profile
        profile = Profile.objects.create(
            # Use the user to create
            user = new_user,
            # Create username, email, first_name
            username = new_user.username,
            email = new_user.email,
            name = new_user.first_name 
        )


'''Anytime delete a profile, it aslo delete the user'''
def deleteUser(sender, instance, **kwargs):
    '''When a profile was deleted, use the profile's instance
       to get the user and user delete method to delete
       the user
    '''
    user = instance.user 
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)

