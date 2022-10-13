# Generated by Django 4.1.2 on 2022-10-12 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_sneakercard_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('number', models.CharField(max_length=1000)),
                ('addres', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=500, verbose_name='Ordered sneakers')),
                ('total_price', models.IntegerField(verbose_name='')),
                ('phone', models.IntegerField(verbose_name='Phone number')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Address')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Sent_at')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer', verbose_name='Сlient')),
            ],
        ),
    ]