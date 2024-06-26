# Generated by Django 4.2.5 on 2023-10-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizzan', '0002_alter_home_image_chef_alter_home_name_chef_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Beef', 'Beef'), ('Chicken', 'Chicken'), ('Fried Rice', 'Fried Rice'), ('Pizza', 'Pizza'), ('Others', 'Others')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_name', models.CharField(max_length=200)),
                ('chef_role', models.CharField(max_length=200)),
                ('chef_image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('food_stock', models.CharField(max_length=100)),
                ('food_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('food_disc', models.CharField(max_length=100)),
                ('food_image', models.ImageField(upload_to='media/')),
                ('food_desc', models.TextField(max_length=200)),
                ('food_reviews', models.CharField(max_length=100)),
                ('food_sku', models.CharField(max_length=100)),
                ('food_category', models.CharField(max_length=100)),
                ('food_tag', models.CharField(max_length=200)),
                ('product_desc', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_name', models.CharField(max_length=200)),
                ('rev_date', models.DateField()),
                ('rev_desc', models.TextField(max_length=200)),
                ('rev_image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]
