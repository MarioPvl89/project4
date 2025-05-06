from django.db import models

class Car(models.Model):
    engine_volume = models.DecimalField(
    max_digits=4, 
    decimal_places=1, 
    default=0.1,
    help_text="Объем двигателя в литрах"
)
    brand = models.CharField("Марка", max_length=100)
    model = models.CharField("Модель", max_length=100)
    year = models.PositiveIntegerField("Год выпуска")
    color = models.CharField("Цвет", max_length=50)
    mileage = models.PositiveIntegerField("Пробег (км)")
    engine_volume = models.DecimalField(max_digits=4, decimal_places=1, help_text="Объем двигателя в литрах")
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=0)
    photo = models.ImageField("Фото", upload_to='catalog/images/cars/')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
