from django.db import models


class Trip(models.Model):
    id = models.IntegerField(primary_key=True)
    trip_name = models.CharField(max_length=32)
    start_date = models.DateField()
    end_date = models.DateField()
    time_created = models.DateField(auto_now_add=True)

    def __repr__(self):
        return f'<Trip #{self.id}: {self.trip_name}>'


class Stop(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=32)
    arrival_date = models.DateField()
    departure_date = models.DateField()

    def __repr__(self):
        return f'<Stop #{self.id}: {self.city_name}>'