# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Crashreport(models.Model):
    id_crash_report = models.AutoField(primary_key=True)
    report_date = models.DateTimeField(blank=True, null=True)
    crashed_machine = models.ForeignKey('Machines', models.DO_NOTHING, db_column='crashed_machine', blank=True, null=True)
    reporting_worker = models.ForeignKey('Personaldata', models.DO_NOTHING, db_column='reporting_worker', blank=True, null=True)
    type = models.CharField(max_length=37, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    repair_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crashReport'


class Machines(models.Model):
    id_machine = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    last_service = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machines'


class Personaldata(models.Model):
    id_personal_data = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    position = models.ForeignKey('WorkerPosition', models.DO_NOTHING, db_column='position', blank=True, null=True)
    login = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    licenses = models.CharField(max_length=22, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personalData'


class WorkerPosition(models.Model):
    id_worker_position = models.AutoField(primary_key=True)
    worker_position_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker_position'
