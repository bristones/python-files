# Generated by Django 3.0.4 on 2020-04-13 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_balance'),
        ('transactions', '0006_transaction_type_trans_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_type', models.CharField(max_length=10)),
                ('trans_code', models.IntegerField()),
                ('sourceAcc', models.IntegerField()),
                ('destAcc', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('time', models.TimeField()),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
            options={
                'db_table': 'genstatement',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Transaction_type',
        ),
    ]