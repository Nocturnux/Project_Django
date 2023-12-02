# Generated by Django 4.2.7 on 2023-12-02 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('typeCabin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('capacity', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('typeCabin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='typeCabin.typecabin')),
            ],
        ),
    ]