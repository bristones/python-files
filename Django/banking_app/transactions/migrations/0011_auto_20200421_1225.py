# Generated by Django 3.0.4 on 2020-04-21 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_auto_20200420_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='all_transactions',
            old_name='service_charge',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='all_transactions',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='all_transactions',
            name='debit',
        ),
        migrations.AlterModelTable(
            name='all_transactions',
            table='transactions',
        ),
    ]
