# Generated by Django 4.1 on 2022-08-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_ordermodel_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='collection_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]