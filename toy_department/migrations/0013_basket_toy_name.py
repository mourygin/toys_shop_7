# Generated by Django 4.2.16 on 2024-10-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy_department', '0012_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='toy_name',
            field=models.CharField(default='', max_length=64),
        ),
    ]
