# Generated by Django 4.1.3 on 2023-01-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mos_sel', '0002_alter_paymentsepd_bill_save_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentsepd',
            name='bill_save_pdf',
            field=models.FileField(upload_to='%d-%m-%Y/', verbose_name='Счет'),
        ),
    ]
