# Generated by Django 4.1.3 on 2023-01-11 11:02

import django.core.files.storage
from django.db import migrations, models
import mos_sel.models


class Migration(migrations.Migration):

    dependencies = [
        ('mos_sel', '0008_alter_paymentsepd_bill_save_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentsepd',
            name='bill_save_pdf',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/Bill_pdf/11-01-2023/<django.db.models.fields.CharField>', location='C:\\Users\\osk88\\Desktop\\Django_projects\\django_selenium\\Bill_pdf\\11-01-2023\\<django.db.models.fields.CharField>'), upload_to=mos_sel.models.PaymentsEpd.get_path, verbose_name='Счет'),
        ),
    ]
