from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True,null=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.OneToOneField(Category,null=True,blank=True,on_delete=models.SET_NULL)
    description = models.TextField("Description",max_length=300)
    images = models.ImageField()

    def __str__(self):
        return self.description
    