# Generated by Django 4.1.6 on 2023-03-11 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinecomposition',
            name='formula_medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.formulamedicine'),
        ),
    ]
