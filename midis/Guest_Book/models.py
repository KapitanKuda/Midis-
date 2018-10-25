from django.db import models
from PIL import Image
# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    email = models.EmailField(max_length=254,db_index=True)
    site = models.URLField(max_length=150,blank=True,null=True)
    body = models.TextField(db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=150,db_index=True)
    browser = models.CharField(max_length=150,db_index=True)
    img = models.ImageField(verbose_name='photo',blank=True, upload_to='users_images',null=True)


    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering=['-date_pub']
