from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str___(self):
        return self.title

class ProductType(models.Model):
    type = models.CharField(max_length=200)

    def __str___(self):
        return self.title

class ProductSubType(models.Model):
    subtype = models.CharField(max_length=200)
    type = models.ForeignKey(ProductType,on_delete=models.CASCADE)
    def __str___(self):
        return self.title


class Product(models.Model):
    productType = models.ForeignKey(ProductSubType,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str___(self):
        return self.title

class Cart(models.Model):
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    # @classmethod
    # def create(cls,item, user):
    #     cart = cls(item=item,user=user)
    #     return cart
    def __str___(self):
        return self.title