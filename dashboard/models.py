from django.db import models

# Create your models here.
#Company Models
class Company(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ('id',)

    def __str__(self):
        return self.name
        

#Product Models
class Product(models.Model):
    name = models.CharField(max_length=50)
    selling_price = models.IntegerField()
    cost_price = models.IntegerField()
    quantity_stock = models.IntegerField()
    product_image = models.ImageField(upload_to = 'products/',blank=True,null=True)
    mfg_date = models.DateField()
    expired_date =models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('id',)

    def __str__(self):
        return self.name