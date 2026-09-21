from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    ROLE_CHOICES = [
        ('wisher', 'wisher'),
        ('angel', 'angel'),
    ]

    full_name = models.CharField(max_length=127, null=True)
    email_address = models.EmailField(max_length=127, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='wisher')
    total_donation = models.DecimalField(max_digits=12, decimal_places=0, default=0, editable=False, null=True)
    fulfilled_count = models.IntegerField(default=0, editable=False, null=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=127, null=True)
    description = models.CharField(max_length=255, null=True)
    icon = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Wishes(models.Model):
    image = models.ImageField(upload_to="wish_image/", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=0, null=True)
    title = models.CharField(max_length=127, null=True)

    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='wishes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='wishes')
    location = models.CharField(max_length=127, null=True)
    beneficiary = models.CharField(max_length=127, null=True)

    progress = models.IntegerField(default=0, editable=False, null=True)
    angels_count = models.IntegerField(default=0, editable=False, null=True)
    views = models.IntegerField(default=0, editable=False, null=True)

    def __str__(self):
        return self.title


class Angel(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='angel', null=True)
    image = models.ImageField(upload_to="angel_image/", null=True)
    tag = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.user.full_name


class Story(models.Model):
    ROLE_CHOICES = [
        ('wisher', 'wisher'),
        ('angel', 'angel'),
    ]

    name = models.CharField(max_length=127, null=True)
    image = models.ImageField(upload_to="story_image/", null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True)
    rating = models.FloatField(default=5.0, null=True)
    text = models.TextField()

    def __str__(self):
        return self.name


class Contribution(models.Model):
    wish = models.ForeignKey(Wishes, on_delete=models.CASCADE, related_name='contributions', null=True)
    angel = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='contributions')
    amount = models.DecimalField(max_digits=12, decimal_places=0)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)