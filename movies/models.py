from django.db import models

class Kategoriler(models.Model):
    name = models.CharField(max_length=40)
    resim = models.CharField(max_length=120)


class Filmler(models.Model):
    film_adi = models.CharField(max_length=100)
    yonetmen = models.CharField(max_length=100)
    aciklama = models.TextField()
    resim = models.CharField(max_length=120)
    anasayfa = models.BooleanField(default=False)


 




