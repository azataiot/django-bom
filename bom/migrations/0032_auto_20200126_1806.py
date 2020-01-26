# Generated by Django 2.2.9 on 2020-01-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0031_auto_20200104_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturerpart',
            old_name='source_mouser',
            new_name='mouser_disable',
        ),
        migrations.AddField(
            model_name='partclass',
            name='mouser_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterIndexTogether(
            name='manufacturerpart',
            index_together=set(),
        ),
    ]
