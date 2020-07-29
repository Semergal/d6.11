from django.db import models

# Create your models here.



class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.CASCADE, blank=True, related_name='books')
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(default = None, max_digits=6, decimal_places=2)
    friend_reader = models.ManyToManyField('p_library.Friend', related_name='book_reader', blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='img/')
    def __str__(self):
        return self.title

class Friend(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    data = models.CharField(max_length=20)
    def __str__(self):
        return self.name


