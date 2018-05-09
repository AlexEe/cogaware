# Generated by Django 2.0.5 on 2018-05-09 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaughtDistortion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caught_at', models.DateTimeField(verbose_name='caught myself at')),
            ],
        ),
        migrations.CreateModel(
            name='DistortionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='caughtdistortion',
            name='distortion_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distortions.DistortionType'),
        ),
    ]
