# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError("User must have an username")

        if not password:
            raise ValueError("User must have password")

        user = self.model(
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return

class Authuser(AbstractBaseUser):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        managed = False
        db_table = 'authUser'


class Crashreport(models.Model):
    id_crash_report = models.AutoField(primary_key=True)
    report_date = models.DateTimeField(blank=True, null=True)
    crashed_machine = models.ForeignKey('Machines', models.DO_NOTHING, db_column='crashed_machine', blank=True, null=True)
    reporting_worker = models.ForeignKey('Personaldata', models.DO_NOTHING, db_column='reporting_worker', blank=True, null=True)
    type = models.CharField(max_length=37, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    urworker = models.CharField(db_column='URWorker', max_length=255, blank=True, null=True)  # Field name made lowercase.
    repair_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crashReport'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    position = models.ForeignKey('WorkerPosition', models.DO_NOTHING, db_column='position', blank=True, null=True)
    credentials = models.ForeignKey(Authuser, on_delete=models.CASCADE, db_column='credentials', blank=True, null=True)
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
