# Generated by Django 2.0.5 on 2018-08-02 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distortions', '0004_auto_20180802_1709'),
    ]

    operations = [
        migrations.RenameModel('CaughtDistortion', 'IdentifiedTrap')
    ]