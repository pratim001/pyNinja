from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=(
        ('ai','AI'),
        ('ml','ML'),
        ('webdev','WEBDEVOPLOPMENT'),
        ('scripting','SCRIPTING'),
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_date='publish')
    body = models.TextField()
    image = models.ImageField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    catagory = models.CharField(max_length=30,choices=STATUS_CHOICES,default='ai')
    
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    
    

