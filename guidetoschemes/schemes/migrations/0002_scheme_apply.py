# Generated by Django 2.1.2 on 2018-10-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheme',
            name='apply',
            field=models.TextField(default=' '),
        ),
    ]
