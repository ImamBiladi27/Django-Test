# Generated by Django 3.2.21 on 2023-09-24 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kategori', models.IntegerField()),
                ('nama_kategori', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_status', models.IntegerField()),
                ('nama_status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_produk', models.IntegerField()),
                ('nama_produk', models.CharField(max_length=255)),
                ('harga', models.IntegerField()),
                ('kategori_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.kategori')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.status')),
            ],
        ),
    ]
