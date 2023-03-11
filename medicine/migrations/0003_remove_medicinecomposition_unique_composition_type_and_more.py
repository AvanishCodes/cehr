# Generated by Django 4.1.6 on 2023-03-11 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_formulamedicine_marketablemedicine_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='medicinecomposition',
            name='unique_composition_type',
        ),
        migrations.AlterField(
            model_name='medicinecomposition',
            name='type',
            field=models.CharField(choices=[('WW', 'Weight to Weight'), ('WV', 'Weight to Volume'), ('VW', 'Volume to Weight'), ('VV', 'Volume to Volume'), ('W', 'Weight'), ('V', 'Volume')], default='WW', max_length=3),
        ),
        migrations.AddConstraint(
            model_name='medicinecomposition',
            constraint=models.UniqueConstraint(fields=('medicine', 'type', 'quantity', 'unit'), name='unique_composition_type'),
        ),
    ]
