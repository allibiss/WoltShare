# Generated by Django 4.1.3 on 2022-11-06 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_product_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='asd', upload_to='products', verbose_name='Image'),
            preserve_default=False,
        ),
    ]