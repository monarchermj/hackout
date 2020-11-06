# Generated by Django 3.1.3 on 2020-11-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='variant',
            field=models.CharField(choices=[('RD', 'Road'), ('SL', 'StreetLight'), ('PW', 'PublicWashroom'), ('SW', 'Sewage'), ('GB', 'Garbage'), ('OR', 'Other')], default='RD', max_length=2),
        ),
    ]
