from django.db import models

class Image(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    original_id = models.IntegerField(db_column='Original_id')
    environment_id = models.IntegerField(db_column='Environment_id')
    filename = models.CharField(max_length=200, db_column='Filename')
    visibility = models.FloatField(db_column='Visibility')

class Session(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    key = models.CharField(max_length=200, db_column='Key')
    global_time = models.IntegerField(db_column='GlobalTime')

class Result(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')
    session = models.ForeignKey(Session, db_column="Session_id")
    image = models.ForeignKey(Image, db_column='Image_id')
    time = models.IntegerField(db_column='Time')
    selection = models.BooleanField(db_column='Selection')
