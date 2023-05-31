from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50, db_index = True)
    
    # slug is used for accesing the category from the url
    slug = models.SlugField(max_length = 255, unique = True)

    # extra info for django
    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('police:category_list', args = [self.slug])
    
    def __str__(self):
        return self.name


class Fine(models.Model):
    category = models.ForeignKey(Category, related_name = 'fine', on_delete = models.CASCADE)

    # what user created the fine
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'fine_creator')
    name = models.CharField(max_length = 50)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(max_length = 50)

    cost = models.DecimalField(max_digits = 7, decimal_places = 2)
    payed = models.BooleanField(default = False)

    # set it only once - at the beginning
    deadline = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Fines'

    def get_absolute_url(self):
        return reverse('police:fine_detail', args = [self.slug])

    def __str__(self):
        return self.name

class Payment(models.Model):
    fine = models.ForeignKey(Fine, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"Payment of {self.amount} for fine: {self.fine.name}"


