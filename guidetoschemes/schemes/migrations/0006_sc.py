# Generated by Django 2.1.2 on 2018-11-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemes', '0005_delete_sch'),
    ]

    operations = [
        migrations.CreateModel(
            name='sc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.CharField(max_length=100)),
                ('d', models.CharField(max_length=30)),
            ],
        ),
    ]
