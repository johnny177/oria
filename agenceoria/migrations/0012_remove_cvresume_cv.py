# Generated by Django 2.2.10 on 2022-09-16 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenceoria', '0011_auto_20220917_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvresume',
            name='cv',
        ),
    ]
