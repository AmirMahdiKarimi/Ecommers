# Generated by Django 4.1.3 on 2022-12-08 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_fly_alter_product_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fly',
        ),
    ]