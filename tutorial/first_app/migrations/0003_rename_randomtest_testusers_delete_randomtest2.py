# Generated by Django 4.0.5 on 2022-06-14 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_randomtest2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RandomTest',
            new_name='TestUsers',
        ),
        migrations.DeleteModel(
            name='RandomTest2',
        ),
    ]
