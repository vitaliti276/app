# Generated by Django 4.0.1 on 2022-02-05 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_new_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='new_field',
        ),
    ]