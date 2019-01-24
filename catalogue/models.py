from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField("カテゴリー", max_length=32)

class Product(models.Model):
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
	name = models.CharField("商品名", max_length=200)
	price = models.PositiveIntegerField("価格")