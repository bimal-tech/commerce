# Generated by Django 3.2 on 2021-04-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_watchlist_total_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='watchlist_total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_item', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='total_item',
        ),
    ]
