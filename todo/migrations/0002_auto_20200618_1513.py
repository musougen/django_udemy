# Generated by Django 2.2 on 2020-06-18 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoProject',
            new_name='TodoModel',
        ),
    ]