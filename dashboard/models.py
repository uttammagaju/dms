from django.db import models

# Create your models here.
#Company Models
class Company(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ('id',)

    def __str__(self):
        return self.name
        

#Product Models
class Product(models.Model):
    name = models.CharField(max_length = 50)
    selling_price = models.IntegerField()
    cost_price = models.IntegerField()
    quantity_stock = models.CharField(max_length = 50)
    product_image = models.ImageField(upload_to = 'products/',blank=True,null=True)
    mfg_date = models.DateField()
    expired_date =models.DateField()
    company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('id',)

    def __str__(self):
        return self.name

#Order Models
class Order(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='orders')
    company = models.ForeignKey(Company,on_delete = models.CASCADE, related_name='orders')
    quantity_order = models.CharField(max_length = 50)
    is_order = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ('id',)

    def __str__(self):
        return self.name