# Generated by Django 4.1.3 on 2022-11-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_image_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default/image.png', upload_to='Categories'),
        ),
    ]
