# Generated by Django 2.1 on 2018-12-27 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_articlestaging'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleStaging',
            new_name='Article_Staging',
        ),
    ]