# Generated by Django 4.2.7 on 2023-12-05 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': [('special_status', 'Can create articles')]},
        ),
    ]