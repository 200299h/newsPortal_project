# Generated by Django 4.1.7 on 2023-04-02 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_category_realted_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='realted_post',
        ),
    ]