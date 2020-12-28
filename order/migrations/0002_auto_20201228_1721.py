# Generated by Django 2.2.5 on 2020-12-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('In Queue', 'In Queue'), ('Processing', 'Processing'), ('Ready', 'Ready'), ('Delivered', 'Delivered'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')], default='In Queue', max_length=256),
        ),
    ]
