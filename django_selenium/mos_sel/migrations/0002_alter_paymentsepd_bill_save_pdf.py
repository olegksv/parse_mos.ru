# Generated by Django 4.1.3 on 2023-01-10 13:04

from django.db import migrations, models
import mos_sel.models


class Migration(migrations.Migration):

    dependencies = [
        ('mos_sel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentsepd',
            name='bill_save_pdf',
            field=models.FileField(upload_to=mos_sel.models.PaymentsEpd.get_path, verbose_name='Счет'),
        ),
    ]