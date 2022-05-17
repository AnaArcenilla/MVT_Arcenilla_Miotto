# Generated by Django 4.0.4 on 2022-05-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.BigIntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('altura', models.FloatField()),
                ('color_de_ojos', models.CharField(max_length=30)),
                ('ocupacion', models.CharField(max_length=30)),
            ],
        ),
    ]
