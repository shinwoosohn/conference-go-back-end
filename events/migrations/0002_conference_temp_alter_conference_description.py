# Generated by Django 4.0.3 on 2023-02-09 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='temp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
