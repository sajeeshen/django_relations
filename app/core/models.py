from django.db import models

# Create your models here.
FOOD_CHOICES = (('Fast Food', 'Fast Food'),
                ('Bar Attached', 'Bar Attached'),
                ('Bakery','Bakery'),('Normal', 'Normal'))

class Place(models.Model):
    """ Model for place """

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)


    def __str__(self):
        return self.name


class Restaurant(models.Model):
    """ Restaurent model """
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    food_choices = models.CharField(choices=FOOD_CHOICES, default='Normal', max_length=50)

    def __str__(self):
        return self.name
    
