# Generated by Django 3.2.3 on 2021-06-08 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.AlterModelTable(
            name='authuser',
            table='authUser',
        ),
    ]
