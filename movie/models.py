from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class  Genre(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    #toString pyton 3
    def __str__(self):
        return self.title

    #toString pyton 2
    def __unicode__(self):
        return self.title


class  Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="judul") #verbose_name digunakaan untuk mengubah nama di UI
    description = models.TextField("deskripsi",null=True, blank=True)#mengubah nama di UI juga bisa di parameter pertama
    show_from = models.DateField()
    show_until = models.DateField()
    genres = models.ManyToManyField(Genre)
    posted_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)#ketika kita membuat pertama kali akan dibuat pawa waktu pertama kali, ketika ada baru gk update
    updated_at = models.DateField(auto_now=True)#ketika membuat pertambahan maka akan diupdate

    #toString pyton 3
    def __str__(self):
        return self.title
    #toString pyton 2
    def __unicode__(self):
        return self.title
    #fungsi Menampilkan macam-macam genre
    def show_genres(self):
        genre = self.genres.all()
        text=''
        for data in genre:
            text += data.title+", "
        return text
    #fungsi untuk menampilkan movie sedang tayang, sudah tayang atau segera tayang dengan representasi angka
    def in_show(self):
        now = datetime.now().date()
        if now >= self.show_from and now <= self.show_until:
            return 1 #sedang tayang
        elif now > self.show_until:
            return -1 #sudah tayang
        else :
            return 0 #segera tayang
    #fungsi untuk menampilkan movie sedang tayang, sudah tayang atau segera tayang dengan representasi angka
    def show_status(self):
        if self.in_show() == 1 :
            return "sedang tayang"
        elif self.in_show()== -1 :
            return "selesai tayang"
        else :
            return "segera tayang"
