from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField(blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    language = models.CharField(max_length=30, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    published_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
