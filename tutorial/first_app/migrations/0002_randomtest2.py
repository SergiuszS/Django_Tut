# Generated by Django 4.0.5 on 2022-06-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomTest2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('second_name', models.CharField(max_length=128)),
            ],
        ),
    ]
