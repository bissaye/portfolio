from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length = 10000)
    subject = models.CharField(max_length = 100000)
    email = models.EmailField(max_length = 100)
    message = models.TextField(max_length = None)
    date = models.DateTimeField(auto_now_add = True)

