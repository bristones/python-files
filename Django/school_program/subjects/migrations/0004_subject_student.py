# Generated by Django 3.0.4 on 2020-03-31 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('subjects', '0003_auto_20200331_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
    ]
