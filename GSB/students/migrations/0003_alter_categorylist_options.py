# Generated by Django 5.0.4 on 2024-05-17 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_categorylist_options_alter_collegelist_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorylist',
            options={'managed': False, 'verbose_name': 'Category List', 'verbose_name_plural': 'Category List'},
        ),
    ]
