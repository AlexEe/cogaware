# Generated by Django 2.0.5 on 2018-05-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distortions', '0002_auto_20180526_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='distortiontype',
            name='description',
            field=models.TextField(null=True),
        ),
    ]