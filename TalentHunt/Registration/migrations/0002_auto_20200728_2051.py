# Generated by Django 3.0.7 on 2020-07-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extuser',
            name='mobile',
            field=models.IntegerField(blank=True),
        ),
    ]
