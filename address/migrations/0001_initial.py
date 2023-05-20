# Generated by Django 4.1.6 on 2023-05-20 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('isd_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('shorthand', models.CharField(max_length=10, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='address.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='address.country')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='address.state')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('al1', models.CharField(max_length=200)),
                ('al2', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='address.city')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='address.state')),
            ],
        ),
    ]
