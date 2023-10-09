from django.db import models


class Category(models.Model):
    """ Model to handle the categories """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Flowers(models.Model):
    """ Model to handle the products """

    class Meta:
        verbose_name_plural = 'Flowers'

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=25, null=True, blank=True)
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    instructions = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name