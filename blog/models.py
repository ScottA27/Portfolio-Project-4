from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from autoslug import AutoSlugField


class Category(models.Model):
    '''The model used for the different categories of blog posts'''
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    ''' The model used for the posts on the blog'''
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', null=False, unique=True, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)
    category = models.ForeignKey(Category, max_length=60, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    '''The model used for the comments on the posts in the blog'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
