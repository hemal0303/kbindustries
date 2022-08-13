from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default = 'default.jpg')

    def __str__(self):
        return (self.name)


class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material = models.CharField(max_length=500, null=True, blank=True)
    mark_type = models.CharField(max_length=50, null=True, blank=True)
    standard = models.CharField(max_length=500, null=True, blank=True)
    size =  models.CharField(max_length=500, null=True, blank=True)
    schedule = models.CharField(max_length=50, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default = 'default.jpg')

    def __str__(self):
        return (self.name)