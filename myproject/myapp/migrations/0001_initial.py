# Generated by Django 4.2.1 on 2023-05-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
