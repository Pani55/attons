from django.db import models


class Product(models.Model):
    """ Model for products """

    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта"
    )
    model = models.CharField(
        max_length=100,
        verbose_name="Модель"
    )
    date_of_release = models.DateField(
        verbose_name="Дата выпуска"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"


class NetworkObject(models.Model):
    """ Model for network objects """

    name = models.CharField(
        max_length=100,
        verbose_name="Название завода"
    )
    email = models.EmailField(
        max_length=100,
        verbose_name="email"
    )
    country = models.CharField(
        max_length=100,
        verbose_name="Страна"
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Город"
    )
    street = models.CharField(
        max_length=100,
        verbose_name="Улица"
    )
    house_number = models.CharField(
        max_length=100,
        verbose_name="Номер дома"
    )
    products = models.ManyToManyField(
        Product,
        verbose_name="Продукты"
    )
    supplier = models.ForeignKey(
        "self",
        verbose_name="Поставщик",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="suppliers"
    )
    debt = models.FloatField(
        verbose_name="Долг",
        default=0
    )
    date_created = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объект сети"
        verbose_name_plural = "Объекты сети"
