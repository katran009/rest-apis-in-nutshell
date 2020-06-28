# Generated by Django 3.0.7 on 2020-06-28 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('website', models.URLField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(choices=[('Red', 'Red'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Indigo', 'Indigo'), ('Violet', 'Violet'), ('White', 'White'), ('Black', 'Black')], default='Black', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('Sneaker', 'Sneaker'), ('Boot', 'Boot'), ('Sandal', 'Sandal'), ('Dress', 'Dress'), ('Other', 'Other')], default='Sneaker', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(default=0)),
                ('brand_name', models.CharField(max_length=30)),
                ('material', models.CharField(max_length=30)),
                ('fasten_type', models.CharField(max_length=30)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ShoeColor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Manufacturer')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ShoeType')),
            ],
        ),
    ]