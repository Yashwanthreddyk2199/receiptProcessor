# Generated by Django 5.2 on 2025-04-13 04:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_rename_short_description_item_shortdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailerreceipt',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
