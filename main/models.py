from django.db import models
from django.core.validators import RegexValidator


class Product(models.Model):
    title = models.CharField(max_length=55)
    price = models.BigIntegerField()
    description = models.CharField(max_length=55)
    image = models.ImageField(upload_to='products_img/')
    text = models.TextField()
    category = models.CharField(max_length=155, choices=[
        ('Fasad', 'Fasad'),
        ('Sokol', 'Sokol'),
        ('Forma', 'Forma')
    ])
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=55)
    img = models.ImageField(upload_to='blog_image/')
    description = models.CharField(max_length=55)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    img = models.ImageField(upload_to='gallery_img/')


class Info(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    tiktok = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)


class Checkout(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message="Telefon raqamingizni to'g'ri ko'rsating.",
            code="Telefon raqam xato"
        )
    ])
    country = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
