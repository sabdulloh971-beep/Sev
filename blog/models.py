from django.db import models
from django.urls import reverse
# Create your models here.
class Contact(models.Model):
    nomi = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    nummer = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.nomi


class Home(models.Model):
    nomi = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text



class Home1(models.Model):
    nomi = models.CharField(max_length=200)
    text = models.TextField()
    rasm = models.ImageField(upload_to='images/')
    nomi1 = models.CharField(max_length=100)
    text1 = models.TextField()
    text2 = models.TextField()


    def __str__(self):
        return self.text


class Home2(models.Model):
    nomi = models.CharField(max_length=200)
    text = models.TextField()
    rasm = models.ImageField(upload_to='images/')
    narx = models.IntegerField()
    nomi1 = models.CharField(max_length=200)
    text1 = models.TextField()
    rasm1 = models.ImageField(upload_to='images/')
    narx1 = models.IntegerField()
    nomi2 = models.CharField(max_length=200)
    text2 = models.TextField()
    rasm2 = models.ImageField(upload_to='images/')
    narx2 = models.IntegerField()

    def __str__(self):
        return self.nomi



class Home3(models.Model):
    nomi = models.CharField(max_length=200)
    text = models.TextField()
    nomi3 = models.CharField(max_length=100)
    nomi1 = models.CharField(max_length=100)
    text1 = models.TextField()
    nomi2 = models.CharField(max_length=100)
    text2 = models.TextField()


    def __str__(self):
        return self.text

class Home4(models.Model):
    nomi = models.CharField(max_length=100)
    madel = models.TextField()
    rasm = models.ImageField(upload_to='images/')
    nomi1 = models.CharField(max_length=100)
    madel1 = models.TextField()
    rasm1 = models.ImageField(upload_to='images/')
    nomi2 = models.CharField(max_length=100)
    madel2 = models.TextField()
    rasm2 = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.nomi


class Home5(models.Model):
    nomi = models.CharField(max_length=200)
    nomi1 = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField()


    def __str__(self):
        return self.nomi



    def get_absolute_url(self):
        return reverse("detel",kwargs={"slug":self.slug})



class Home6(models.Model):
    rasm = models.ImageField(upload_to='images/')
    nomi = models.CharField(max_length=200)
    text = models.TextField()
    rasm1 = models.ImageField(upload_to='images/')
    nomi1 = models.CharField(max_length=200)
    text1 = models.TextField()
    rasm2 = models.ImageField(upload_to='images/')
    nomi2 = models.CharField(max_length=200)
    text2 = models.TextField()
    rasm3 = models.ImageField(upload_to='images/')
    nomi3 = models.CharField(max_length=200)
    text3= models.TextField()


    def __str__(self):
        return self.nomi