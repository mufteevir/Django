from django.db import models as models

class EventEv(models.Model):
    id = models.IntegerField(primary_key=True)
    eventname = models.CharField(db_column='eventName', max_length=30)  # Field name made lowercase.

    def __str__(self):
        return self.eventname

    class Meta:

        db_table = 'eventev'

class Lines(models.Model):
    id = models.IntegerField(primary_key=True)
    linename = models.CharField(db_column='lineName', max_length=20)  # Field name made lowercase.

    def __str__(self):
        return self.linename

    class Meta:

        db_table = 'lines'




class Presentations(models.Model):
    lineid = models.ForeignKey(Lines, on_delete=models.PROTECT, db_column='line_id')  # Field name made lowercase.
    masterid = models.ForeignKey('bboard.masters', on_delete=models.PROTECT,  db_column='master_id')  # Field name made lowercase.
    diename = models.CharField(db_column='dieName', max_length=50)  # Field name made lowercase.
    eventid = models.ForeignKey(EventEv, on_delete=models.PROTECT,  db_column='event_id')  # Field name made lowercase.
    eventval0 = models.CharField(db_column='eventVal0', max_length=16)  # Field name made lowercase.
    eventval1 = models.CharField(db_column='eventVal1', max_length=16)  # Field name made lowercase.
    eventtime = models.DateTimeField(primary_key=True, db_column='EventTime')  # Field name made lowercase.
    #id = models.AutoField(db_column='ID')  # Field name made lowercase.

    class Meta:

        db_table = 'presentations'
        #ordering = ['-id']


