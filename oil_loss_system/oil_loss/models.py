from django.db import models

# Модель нефтепродукта
class OilProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    density = models.FloatField(help_text="Плотность, кг/м³", verbose_name="Плотность")
    evaporation_rate = models.FloatField(help_text="Коэффициент испарения", verbose_name="Коэффициент испарения")

    def __str__(self):
        return self.name

# Модель хранилища
class Storage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название хранилища")
    capacity = models.FloatField(help_text="Емкость, м³", verbose_name="Емкость")
    location = models.CharField(max_length=100, verbose_name="Расположение")

    def __str__(self):
        return self.name

# Модель транзакции (учет потерь)
class Transaction(models.Model):
    oil_product = models.ForeignKey(OilProduct, on_delete=models.CASCADE, verbose_name="Нефтепродукт")
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, verbose_name="Хранилище")
    initial_volume = models.FloatField(help_text="Начальный объем, м³", verbose_name="Начальный объем")
    final_volume = models.FloatField(help_text="Конечный объем, м³", verbose_name="Конечный объем")
    temperature = models.FloatField(help_text="Температура, °C", verbose_name="Температура")
    date = models.DateField(verbose_name="Дата")

    def calculate_loss(self):
        """Метод расчета естественной убыли"""
        return max(self.initial_volume - self.final_volume, 0)

    def __str__(self):
        return f"{self.oil_product.name} - {self.date}"


from django.db import models


class OilProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    density = models.FloatField(help_text='Плотность, кг/м³', verbose_name='Плотность')
    evaporation_rate = models.FloatField(help_text='Коэффициент испарения', verbose_name='Коэффициент испарения')

    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название хранилища')
    capacity = models.FloatField(help_text='Емкость, м³', verbose_name='Емкость')
    location = models.CharField(max_length=100, verbose_name='Расположение')

    def __str__(self):
        return self.name


class Transaction(models.Model):
    initial_volume = models.FloatField(help_text='Начальный объем, м³', verbose_name='Начальный объем')
    final_volume = models.FloatField(help_text='Конечный объем, м³', verbose_name='Конечный объем')
    temperature = models.FloatField(help_text='Температура, °C', verbose_name='Температура')
    date = models.DateField(verbose_name='Дата')
    oil_product = models.ForeignKey('OilProduct', on_delete=models.CASCADE, verbose_name='Нефтепродукт')
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE, verbose_name='Хранилище')

    # Поле для естественной убыли
    natural_loss = models.FloatField(default=0, verbose_name='Естественная убыль')

    def calculate_natural_loss(self):
        """Метод для расчета естественной убыли."""
        evaporation_rate = self.oil_product.evaporation_rate
        self.natural_loss = self.initial_volume * (0.001 * self.temperature * evaporation_rate)
        return self.natural_loss

    def save(self, *args, **kwargs):
        self.calculate_natural_loss()
        super().save(*args, **kwargs)


from django.db import models

class Storage(models.Model):
    # Поля для модели Storage
    name = models.CharField(max_length=100, verbose_name='Название хранилища')
    capacity = models.FloatField(help_text='Емкость, м³', verbose_name='Емкость')
    location = models.CharField(max_length=100, verbose_name='Расположение')

class Transaction(models.Model):
    # Поля для модели Transaction
    initial_volume = models.FloatField(help_text='Начальный объем, м³', verbose_name='Начальный объем')
    final_volume = models.FloatField(help_text='Конечный объем, м³', verbose_name='Конечный объем')
    temperature = models.FloatField(help_text='Температура, °C', verbose_name='Температура')
    date = models.DateField(verbose_name='Дата')
    oil_product = models.ForeignKey('OilProduct', on_delete=models.CASCADE, verbose_name='Нефтепродукт')
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, verbose_name='Хранилище', null=True, blank=True)  # сделано необязательным

    def __str__(self):
        return f"Транзакция {self.id} для {self.oil_product.name}"
