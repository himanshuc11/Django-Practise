# Generated by Django 4.0.1 on 2022-01-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=128)),
                ('last', models.CharField(max_length=128)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
    ]
