# Generated by Django 4.1.6 on 2023-05-13 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('prescription', '0004_dosage_alter_prescription_dosage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='address',
        ),
        migrations.AddField(
            model_name='visit',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='address.address'),
        ),
    ]