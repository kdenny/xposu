from django.db import models
from djgeojson.fields import PointField
from datetime import date


# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    address = models.TextField(max_length=200)
    city = models.TextField(max_length=200)

    def __unicode__(self):
        return unicode(self.name)


class Complaint(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    type = models.CharField(max_length=40)
    value = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    comments = models.TextField(max_length=500)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        # return unicode(self.id)
        # return u"Game ID {0} between {1} and {2}".format(self.id, self.home_team, self.away_team)
        return unicode(self.id)
