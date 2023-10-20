# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Board(models.Model):
    boardno = models.AutoField(db_column='boardNo', primary_key=True)  # Field name made lowercase.
    boardtitle = models.CharField(db_column='boardTitle', max_length=300)  # Field name made lowercase.
    boardcontent = models.CharField(db_column='boardContent', max_length=2000)  # Field name made lowercase.
    mid = models.CharField(db_column='mId', max_length=50)  # Field name made lowercase.
    boarddate = models.DateTimeField(db_column='boardDate')  # Field name made lowercase.
    boardcount = models.DecimalField(db_column='boardCount', max_digits=10, decimal_places=0)  # Field name made lowercase.
    last_dt = models.DateTimeField(db_column='LAST_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Board'


class Smember(models.Model):
    mid = models.CharField(db_column='mID', primary_key=True, max_length=100)  # Field name made lowercase.
    mname = models.CharField(db_column='mName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mmode = models.CharField(db_column='mMode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mpw = models.CharField(db_column='mPW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    malias = models.CharField(db_column='mAlias', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mbirth = models.CharField(db_column='mBirth', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mzip_cd = models.CharField(db_column='mZIP_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    maddr = models.CharField(db_column='mADDR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mdetl_addr = models.CharField(db_column='mDETL_ADDR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mphone = models.CharField(db_column='mPHONE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    memail = models.CharField(db_column='mEMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mmemo = models.CharField(db_column='mMEMO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    inst_dt = models.DateTimeField(db_column='INST_DT', blank=True, null=True)  # Field name made lowercase.
    last_dt = models.DateTimeField(db_column='LAST_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sMember'
