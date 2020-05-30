# Generated by Django 3.0.6 on 2020-05-30 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
        ('products', '0002_products_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='cart_desc',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_season', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('discount', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Products')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Products')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Users')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT,
                                    to='products.Subcategories'),
        ),
    ]