# projects/models.py

# Django modules
from django.db import models
import uuid 

# Locals

# Create your models here.

# MODELS:Project
class Project(models.Model):
	
    '''NOTE:
	   Project adalah nama tabel di dalam database
	   yang berisi kolom-kolom: title, description
	   demo_link, source_link, created dan id.
    '''
    title = models.CharField(
                max_length=200)
    description = models.TextField(
                null=True, blank=True)
    demo_link = models.CharField(
                max_length=2000, null=True, blank=True)
    source_link = models.CharField(
                max_length=2000, null=True, blank=True)
    created = models.DateTimeField(
                auto_now_add=True)
    ''' Menggunakan uuid berarti:
        1. Mengesampingkan default id pada tabel.
        2. Menggunakannya sebagai Primary Key.
        3. uuid tidak bisa diedit. '''
    id = models.UUIDField(
                default=uuid.uuid4, unique=True,
                primary_key=True, editable=False)











