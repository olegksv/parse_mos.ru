from django.contrib import admin
from mos_sel.models import Flat

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    # list_display list_filter это обязательные названия имена опций (именно так надо писать) для изменения отображения полей в админке
    list_display=('id','name_flat','cod_platelshika','period_oplaty','summa')
