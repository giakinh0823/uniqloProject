# Generated by Django 3.1.5 on 2021-01-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phonenumber',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
