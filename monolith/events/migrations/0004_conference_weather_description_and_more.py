# Generated by Django 4.0.3 on 2023-02-09 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_conference_lat_conference_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='weather_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='description',
            field=models.TextField(),
        ),
    ]