# Generated by Django 3.1.5 on 2021-01-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210110_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateTimeField(help_text='Select today/now as the input\n                                                  if the product is being\n                                                  published now.', verbose_name='product release date'),
        ),
    ]
