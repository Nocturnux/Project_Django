# Generated by Django 4.2.7 on 2023-12-07 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabin', '0001_initial'),
        ('reservation_sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation_cabin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('Cabin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cabin.cabin')),
                ('reservation_sale', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reservation_sale.reservation_sale')),
            ],
        ),
    ]
