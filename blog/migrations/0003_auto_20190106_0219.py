# Generated by Django 2.1 on 2019-01-06 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190106_0211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='tag',
        ),
    ]
