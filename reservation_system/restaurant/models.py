from django.db import models

# Create your models here.
class Table(models.Model):

    def __str__(self) -> str:
        return f'Table-{self.id}'


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    time_of_reservation = models.DateTimeField(auto_now=True)
    people_count = models.IntegerField()
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()

    def __str__(self) -> str:
        return f'Reservation{self.id} - {self.table}'


