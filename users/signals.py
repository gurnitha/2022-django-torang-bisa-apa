# users/signals.py

# Django modules
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

# Locals
from .models import Profile

# Step 4: Real live using Signals
# Create a new user --> a new user's profile will 
# also be created automatically

# NOTE:
# 1. User dibuat, profile terbuat
# 2. User dihapus, profile terhapus
# 3. Profile dihapus, user juga terhapus
#------------------------------------------------

# Signals
# @receiver(post_save, sender=Profile)
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