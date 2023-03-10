# Generated by Django 4.1.3 on 2022-11-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, auto_created='djangodbmodelsfieldscharfield', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, auto_created='djangodbmodelsfieldscharfield', unique=True),
        ),
    ]
