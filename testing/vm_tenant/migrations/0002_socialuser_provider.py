# Generated by Django 3.1.4 on 2021-10-11 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vm_tenant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialuser',
            name='provider',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
