# Generated by Django 3.0.7 on 2020-08-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualskills',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]