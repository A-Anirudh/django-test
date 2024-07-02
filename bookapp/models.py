from django.db import models

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='img/')

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Publisher(models.Model):
    name = models.CharField(max_length=10)
    website = models.URLField()
    publisher_date = models.DateField()

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=10)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publisher_date = models.DateField()

    def __str__(self):
        return f"{self.title}"
