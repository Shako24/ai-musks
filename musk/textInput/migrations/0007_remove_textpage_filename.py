# Generated by Django 4.1.2 on 2022-11-23 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("textInput", "0006_textpage_filename"),
    ]

    operations = [
        migrations.RemoveField(model_name="textpage", name="fileName",),
    ]