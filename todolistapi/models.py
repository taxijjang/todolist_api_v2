from django.db import models
from django.utils import timezone

class DoTitle(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add='True', null = True)

    def __str__(self):
        return self.title


class DoList(models.Model):
    title = models.ForeignKey(DoTitle, related_name= 'dolist', on_delete= models.CASCADE)
    list = models.CharField(max_length=200)

    def __str__(self):
        return self.list

class DoComment(models.Model):
    title = models.ForeignKey(DoTitle, related_name='docomment', on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment#