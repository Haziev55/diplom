# Generated by Django 3.2.25 on 2024-11-11 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oil_loss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='natural_loss',
            field=models.FloatField(default=0, verbose_name='Естественная убыль'),
        ),
    ]
