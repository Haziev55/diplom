# Generated by Django 3.2.25 on 2024-11-11 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OilProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('density', models.FloatField(help_text='Плотность, кг/м³', verbose_name='Плотность')),
                ('evaporation_rate', models.FloatField(help_text='Коэффициент испарения', verbose_name='Коэффициент испарения')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название хранилища')),
                ('capacity', models.FloatField(help_text='Емкость, м³', verbose_name='Емкость')),
                ('location', models.CharField(max_length=100, verbose_name='Расположение')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_volume', models.FloatField(help_text='Начальный объем, м³', verbose_name='Начальный объем')),
                ('final_volume', models.FloatField(help_text='Конечный объем, м³', verbose_name='Конечный объем')),
                ('temperature', models.FloatField(help_text='Температура, °C', verbose_name='Температура')),
                ('date', models.DateField(verbose_name='Дата')),
                ('oil_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oil_loss.oilproduct', verbose_name='Нефтепродукт')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oil_loss.storage', verbose_name='Хранилище')),
            ],
        ),
    ]