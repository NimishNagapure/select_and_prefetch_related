# Generated by Django 3.2.4 on 2021-06-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]
