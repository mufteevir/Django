from django.db import models

# Create your models here.


class Thickness(models.Model):
    diename = models.CharField(db_column='dieName', max_length=20)  # Field name made lowercase.
    tolerancem = models.CharField(db_column='toleranceM', blank=True, null=True, max_length= 5)  # Field name made lowercase.
    actualthickness = models.CharField(db_column='actualThickness', blank=True, null=True, max_length= 5)  # Field name made lowercase.
    tolerancep = models.CharField(db_column='toleranceP', blank=True, null=True, max_length= 5)  # Field name made lowercase.
    measuringerror = models.BooleanField(db_column='measuringError', blank=True, null=True)  # Field name made lowercase.
    eventtime = models.DateTimeField(primary_key=True, db_column='EventTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'thickness'