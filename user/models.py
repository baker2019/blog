from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=60,null=False)

    def __str__(self):
        return f'{self.name}'
        
class City(models.Model):
    name = models.CharField(max_length=60,null=False)
    country = models.ForeignKey(to="Country",on_delete=models.CASCADE,related_name="city_set")

    def __str__(self):
        return f'{self.name}'