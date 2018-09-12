from django.db import models
from django.contrib.auth.models import User
from pytils import translit


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = translit.slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Page(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = translit.slugify(self.title)
        super(Page, self).save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
