# Generated by Django 2.2.5 on 2021-03-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperAdmin', '0002_auto_20210317_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasma',
            name='donor_name',
            field=models.CharField(max_length=35, verbose_name='Donor Name'),
        ),
    ]