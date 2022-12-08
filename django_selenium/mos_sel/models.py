from django.db import models

class Flat(models.Model):
    name_flat=models.CharField(max_length=50,verbose_name="Название квартиры")
    cod_platelshika=models.CharField(max_length=50,db_index=True, verbose_name="Код плательщика")
    period_oplaty=models.CharField(max_length=50,verbose_name='Период оплаты')
    summa=models.CharField(max_length=50,verbose_name="Сумма счета")

    def __str__(self) -> str:
        return f'{self.name_flat}'