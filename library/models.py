from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.first_name}'

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=300)
    summary = models.TextField()
    isbn = models.IntegerField()
    author = models.ForeignKey(to='Author',
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    genre = models.ManyToManyField(to='Genre')
    def __str__(self):
        return self.title

class BookInstance(models.Model):
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    due_back = models.DateField()
    reader = models.ForeignKey(to=User,
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    LOAN_STATUS = (
        ('d', 'Administered'),
        ('t', 'Taken'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(choices=LOAN_STATUS, default='d')

    def __str__(self):
        return f'{self.book}'
