from django.contrib import admin
from mos_sel.models import Flat,PaymentsEpd

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    # list_display list_filter это обязательные названия имена опций (именно так надо писать) для изменения отображения полей в админке
    #list_display=('id','name_flat','cod_platelshika','period_oplaty','summa')
    list_display=('id','name_flat',)

@admin.register(PaymentsEpd)
class PaymentsEpdAdmin(admin.ModelAdmin):
    # list_display list_filter это обязательные названия имена опций (именно так надо писать) для изменения отображения полей в админке
    list_display=(  'id',
                    'flats_id',
                    'name_flat',
                    'date_pars',
                    'cod_platelshika',
                    'period_oplaty',
                    'summa',
                    'bill_save_pdf',
                    'amount_of_real',
                    'date_of_payment'
                    )
