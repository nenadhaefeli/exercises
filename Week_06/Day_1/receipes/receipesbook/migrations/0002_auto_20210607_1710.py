# Generated by Django 3.2.4 on 2021-06-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipesbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipemodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='receipemodel',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
    ]