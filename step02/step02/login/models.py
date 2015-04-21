from django.db import models

# Create your models here.

class user_register(models.Model):
    user_name = models.CharField(max_length = 30, default = None)
    user_email = models.EmailField()
    user_passwd = models.CharField(max_length = 30, default = None)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class pr(models.Model):
    photo_id = models.CharField(max_length=20)
    photo_path =models.CharField(max_length=200)
    photo_size = models.IntegerField()
    photo_type = models.CharField(max_length=8)
    browse_times = models.IntegerField(default=1)
    user_name = models.CharField(max_length = 30, default =None)
    photo_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photo_path , self.photo_size

