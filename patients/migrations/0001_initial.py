# Generated by Django 2.0.7 on 2018-07-29 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(max_length=6)),
                ('status', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('g', models.IntegerField()),
                ('p', models.IntegerField()),
                ('a1', models.IntegerField()),
                ('a2', models.IntegerField()),
                ('a3', models.IntegerField()),
                ('a4', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('religion', models.CharField(max_length=50)),
            ],
        ),
    ]