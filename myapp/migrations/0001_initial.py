# Generated by Django 5.0.6 on 2024-06-12 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('client', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('url', models.URLField()),
                ('picture1', models.ImageField(upload_to='media')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='media')),
                ('picture3', models.ImageField(blank=True, null=True, upload_to='media')),
                ('text', models.TextField()),
                ('authter', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]
