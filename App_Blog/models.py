from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    blog_title = models.CharField(max_length=264,verbose_name="Put a title") # Verbose acts as a placeholder
    slug = models.SlugField(max_length=264,unique=True) # Slug field is used to give the website url the same name as your title name
    blog_content = models.TextField(verbose_name="What is on your mind?")
    blog_image = models.ImageField(upload_to="blog_images",verbose_name="Blog image")
    publish_date = models.DateTimeField(auto_now_add=True) # auto_now_add is used to enter time and date automatically when something is created
    update_date = models.DateTimeField(auto_now=True) # auto_now is used to enter time and date automatically when something is updated

    def __str__(self):
        return self.blog_title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog,related_name="blog_comment",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="user_comment",on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    

class Likes(models.Model):
    blog = models.ForeignKey(Blog,related_name="liked_blog",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="liker_user",on_delete=models.CASCADE)