import os
from django.db import models
from pytils.translit import slugify
from pathlib import Path
from datetime import date
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class Flat(models.Model):
    name_flat=models.CharField(max_length=50, unique=True,db_index=True, verbose_name="Название квартиры")
    #name_flat=models.CharField(max_length=50,verbose_name="Название квартиры")
    #cod_platelshika=models.CharField(max_length=50,db_index=True, verbose_name="Код плательщика")
    #period_oplaty=models.CharField(max_length=50,verbose_name='Период оплаты')
    #summa=models.CharField(max_length=50,verbose_name="Сумма счета")

    def __str__(self) -> str:
        return f'{self.name_flat}'




class PaymentsEpd(models.Model):
    flats=models.ForeignKey(Flat,on_delete=models.PROTECT)
    name_flat=models.CharField(max_length=60,verbose_name="Название квартиры" )
    date_pars=models.DateTimeField(auto_now=True,null=True)
    cod_platelshika=models.CharField(max_length=50,db_index=True, verbose_name="Код плательщика")
    """ period_oplaty=models.CharField(max_length=50,verbose_name='Период оплаты') """
    period_oplaty=models.DateField(verbose_name='Период оплаты')
    summa=models.CharField(max_length=50,verbose_name="Сумма счета")
    amount_of_real=models.DecimalField(max_digits=10,decimal_places=2, verbose_name="Оплачено")
    date_of_payment=models.DateField(verbose_name="Дата оплаты счета",null=True)
    #bill_save_pdf=models.FileField(upload_to='Bill_pdf/%d/%m/%Y/', verbose_name="Счет")
    #bill_save_pdf=models.FileField(upload_to='Bill_pdf/%d-%m-%Y/"{flats}"'.format(flats=name_flat.upper()), verbose_name="Счет")
    """ def get_new_path(instance,filename):
        path="{0}/{1}/{2}".format(date.today().strftime("%d-%m-%Y"),instance.flats.name_flat,filename)
        print(path)
        return path """
    """ def get_path(self,filename):
        return f'{self.flats}/{filename}'
    bill_save_pdf=models.FileField(upload_to=get_path, verbose_name="Счет") """
    
    
    def get_path(instance, filename):
        ext = os.path.splitext(filename)
        filename = "%s.%s" % (instance.period_oplaty, ext[1])
        return os.path.join(settings.MEDIA_ROOT, filename)

    """  def get_path(self,filename):
        return '{0}-{1}-{2}/{3}/{4}'.format(
            date.today().strftime('%d'),
            date.today().strftime('%m'),
            date.today().strftime('%Y/'),
            self.flats.name_flat,
            filename)       """                          
    
    """ bill_save_pdf=models.FileField(upload_to=get_path, verbose_name="Счет",
                                   storage=FileSystemStorage(
                                   location=settings.BILL_FILES_PATH + "\\"+str(name_flat),
                                   base_url=os.path.join(settings.MEDIA_URL,settings.BILL_MEDIA_URL+"/"+str(name_flat)))
    
                                   )   """
    """  def storage_path():
        fs_path=FileSystemStorage(location=)
        return fs_path """
    bill_save_pdf=models.FileField(upload_to=get_path, verbose_name="Счет",)           
                                      
    #bill_save_pdf=models.FileField(upload_to=get_path, verbose_name="Счет")
    def __str__(self) -> str:
        return f'{self.name_flat}'


    class Meta:
        verbose_name='Оплата'
        verbose_name_plural='Оплаты'
        ordering=['name_flat']

    