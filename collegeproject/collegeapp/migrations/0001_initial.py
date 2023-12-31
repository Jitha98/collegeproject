# Generated by Django 4.2.3 on 2023-11-17 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField(max_length=8)),
                ('age', models.IntegerField()),
                ('gender', models.TextField()),
                ('phno', models.IntegerField()),
                ('email', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=250)),
                ('courses', models.CharField(max_length=250)),
                ('purposes', models.CharField(max_length=250)),
                ('materials', models.TextField()),
            ],
        ),
    ]
