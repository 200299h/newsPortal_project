# Generated by Django 4.1.7 on 2023-03-30 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_categorys_post_remove_posts_main_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='main_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_cat', to='posts.categorys'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post',
            field=models.ManyToManyField(related_name='cat', to='posts.categorys'),
        ),
    ]
