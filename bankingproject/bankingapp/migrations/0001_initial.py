# Generated by Django 4.2.5 on 2023-09-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('account_type', models.CharField(max_length=20)),
                ('debit_card', models.BooleanField(default=False)),
                ('credit_card', models.BooleanField(default=False)),
                ('district', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
    ]