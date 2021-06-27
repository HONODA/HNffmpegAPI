# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HnVideo(models.Model):
    md = models.CharField(max_length=255)
    url = models.CharField(max_length=2000)
    path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hn_video'


class UserLog(models.Model):
    userid = models.BigIntegerField(db_column='userId', primary_key=True)  # Field name made lowercase.
    opedate = models.DateTimeField()
    pushback = models.IntegerField()
    url = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'user_log'
