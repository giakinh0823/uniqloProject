# Generated by Django 2.2.5 on 2020-12-21 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appProduct', '0006_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]