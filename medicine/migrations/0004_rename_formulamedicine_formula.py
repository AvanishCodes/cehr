# Generated by Django 4.1.6 on 2023-03-11 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_rename_formula_medicine_medicinecomposition_formula'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormulaMedicine',
            new_name='Formula',
        ),
    ]