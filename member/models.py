from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20)
    prof_pic = models.ImageField("Photo Profile",upload_to='prof_pic/',null=True, blank=True)
    register_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    #fungsi untuk mengambil password dari user
    def user_password(self):
        return self.user.password

class TopUp(models.Model):
    #variabel ini ditulis dengan huruf besar berarti di merupakan tetapan /static final
    STATUS_CHOICES = (('p','pending'),('v','valid'),('i','invalid'))
    member = models.ForeignKey(Member)
    amount = models.IntegerField()
    receipt = models.ImageField("Bukti Bayar", upload_to='receipts/')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    validated_at = models.DateTimeField(auto_now=True)
    checked_by = models.ForeignKey(User, null=True,blank=True)
