# Generated by Django 4.2 on 2023-04-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.TextField()),
                ('amount', models.FloatField()),
                ('n_orders', models.IntegerField()),
                ('init_price', models.FloatField()),
                ('rate_changes', models.IntegerField()),
                ('martingale', models.IntegerField()),
                ('f_order_indent', models.FloatField()),
                ('commission', models.FloatField()),
                ('algorithm', models.CharField(choices=[('long', 'Long'), ('short', 'Short')], default='short', max_length=5)),
            ],
        ),
    ]
