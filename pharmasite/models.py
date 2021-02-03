from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    new_product = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    fast_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    subject = models.TextField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject
