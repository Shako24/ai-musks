# Generated by Django 3.2.5 on 2022-10-08 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0004_alter_aiproject_colorscheme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiproject',
            name='customPageName',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
