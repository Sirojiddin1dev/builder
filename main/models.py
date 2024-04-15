from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=55)
    image = models.ImageField(upload_to='products_img/')
    text = models.TextField()
    PRODUCT = (
        ('Fasad','Fasad'),
        ('Sokol','Sokol'),
        ('Forma','Forma')
    )
    category = models.CharField(max_length=55, choices=PRODUCT)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=55)
    img = models.ImageField(upload_to='blog_image/')
    description = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now=True)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='about_img/')
    text = models.TextField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    img = models.ImageField(upload_to='gallery_img/')



