# Generated by Django 3.2.4 on 2021-07-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='media/foods/images')),
                ('desc', models.TextField()),
                ('food_cateogry_id', models.BigIntegerField()),
                ('food_cost', models.DecimalField(decimal_places=4, max_digits=9)),
                ('sale_price', models.DecimalField(decimal_places=4, max_digits=9)),
                ('markup', models.FloatField()),
            ],
            options={
                'db_table': 'foods',
            },
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='media/food_category/images')),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 'foods_categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('client_phone', models.CharField(max_length=255)),
                ('client_address', models.CharField(max_length=255)),
                ('client_location', models.CharField(max_length=255)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(max_length=255)),
                ('order_sum', models.DecimalField(decimal_places=4, max_digits=20)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.BigIntegerField()),
                ('food_id', models.BigIntegerField()),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 'orders_description',
            },
        ),
    ]
