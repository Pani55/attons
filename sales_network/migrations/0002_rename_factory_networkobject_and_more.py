# Generated by Django 4.2.2 on 2024-11-08 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sales_network", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Factory",
            new_name="NetworkObject",
        ),
        migrations.AlterModelOptions(
            name="networkobject",
            options={
                "verbose_name": "Объект сети",
                "verbose_name_plural": "Объекты сети",
            },
        ),
    ]
