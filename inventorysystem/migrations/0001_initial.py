# Generated by Django 3.1.4 on 2021-02-06 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_brand', models.CharField(max_length=200)),
                ('store_addr', models.CharField(max_length=200)),
                ('store_category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_name', models.CharField(max_length=200)),
                ('inventory_amount', models.IntegerField(default=0)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventorysystem.store')),
            ],
        ),
    ]
