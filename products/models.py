from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    summary = models.TextField(default='This is cool')
    feature = models.BooleanField(null=True)

    # def get_absolute_url(self,*args,**kwargs):
    #     return f"/product/{self.id}/"

    
    # def get_absolute_url(self,*args,**kwargs):
    #     """

    #       We are using this method to call using namespace url that reason reverse name

    #     """
    #     return reverse("products-detail" , kwargs={"id" : self.id})

    def get_absolute_url(self,*args,**kwargs):
        """

          We are using this method to reverse using namespace also

        """
        return reverse("products:products-detail" , kwargs={"id" : self.id})