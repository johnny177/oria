# Generated by Django 2.2.10 on 2022-09-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenceoria', '0008_auto_20220914_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='max_booking',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='number_booking',
            field=models.IntegerField(null=True),
        ),
    ]
