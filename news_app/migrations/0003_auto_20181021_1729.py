# Generated by Django 2.1 on 2018-10-21 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_auto_20181021_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='region_category_id',
            new_name='region_category',
        ),
        migrations.RenameField(
            model_name='userquery',
            old_name='region_id',
            new_name='region',
        ),
    ]