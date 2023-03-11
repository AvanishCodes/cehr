# Generated by Django 4.1.6 on 2023-03-11 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0006_remove_medicinecomposition_unique_composition_type'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='medicinecomposition',
            constraint=models.UniqueConstraint(fields=('formula_medicine', 'molecule'), name='unique_composition_type'),
        ),
    ]