# Generated by Django 5.1.5 on 2025-02-05 13:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_siteinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='headertext',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
