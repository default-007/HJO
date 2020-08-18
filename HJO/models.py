from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=250, blank=True)
    tag = models.CharField(max_length= 100, blank=True, null=True)
    author = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    post = models.TextField(max_length=52500, blank=True)

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return f"/post/{self.id}"

    @property
    def get_all_comments(self):
        return self.comments.all()

    @property
    def get_all_tags(self):
        return tags.all()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    comment = models.TextField(max_length=5500, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=250, blank=True)
    email= models.EmailField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.comment}'

    class Meta:
        ordering = ["-pk"]


class Testimonial(models.Model):
    pic = models.ImageField(upload_to='posts/')
    position = models.CharField(max_length=250, blank=True)
    name = models.CharField(max_length=250, blank=True)
    testimony = models.TextField(max_length=52500, blank=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f'{self.title}'