# Generated by Django 3.0.5 on 2020-04-09 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200409_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='cruises',
            field=models.ManyToManyField(to='main_app.RiverCruise'),
        ),
    ]