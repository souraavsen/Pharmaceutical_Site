from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    p_type = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def write(self):
        return self.description[:100] + '...Learn more '
