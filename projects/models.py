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

    def __str__(self):
        return self.title



# MODELS:Review
class Review(models.Model):

    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    '''
    Menambahkan field 'project' pada model Review,
    seperti terlihat di bahwa ini, dimaksudkan untuk
    membuat hubungan OneToMany antara model Project dan Review.

    Hal itu berarti bahwa sebuah proyek dapat memiliki
    0 atau 1 atau banyak reeview. Dengan kata lain 
    setiap Review ditujukan hanya untuk sebuah Proyek. 

    Jadi sebuah proyek ada kemungkinan memiliki 
    banyak Review, sebuah review atau tidak sama 
    sekali memiliki review.
    '''
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE)
    body = models.TextField(
        null=True, 
        blank=True)
    value = models.CharField(
        max_length=200, 
        choices=VOTE_TYPE)
    created = models.DateTimeField(
        auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True,
        primary_key=True, 
        editable=False)

    def __str__(self):
        return self.value



# MODELS:Tag
class Tag(models.Model):
    name = models.CharField(
        max_length=200)
    created = models.DateTimeField(
        auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True,
        primary_key=True, 
        editable=False)

    def __str__(self):
        return self.name






