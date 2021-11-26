# Generated by Django 3.2.4 on 2021-11-21 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RatesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_Name', models.CharField(max_length=200)),
                ('Pub_Date', models.DateTimeField(verbose_name='date published')),
                ('Price', models.IntegerField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.ratescategory')),
            ],
        ),
    ]