from django.db import models

# Create your models here.
FOOD_CHOICES = (('Fast Food', 'Fast Food'),
                ('Bar Attached', 'Bar Attached'),
                ('Bakery','Bakery'),('Normal', 'Normal'))

class TimeStamp(models.Model):
    """ Generic model for all model timestamp"""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Place(TimeStamp, models.Model):
    """ Model for place. Also inhering Timestamp abstract model """

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)


    def __str__(self):
        return self.name


class Restaurant(TimeStamp, models.Model):
    """ Restaurent model """
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    food_choices = models.CharField(choices=FOOD_CHOICES, default='Normal', max_length=50)

    def __str__(self):
        return self.name
    
