# Generated by Django 2.1 on 2022-12-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=16, unique=True, verbose_name='姓名'),
        ),
    ]