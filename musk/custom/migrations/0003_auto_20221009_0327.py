# Generated by Django 3.2.5 on 2022-10-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_aiproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='aiproject',
            name='customPageName',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='aiproject',
            name='aboutPage',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='aiproject',
            name='colorScheme',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='aiproject',
            name='contactPage',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='aiproject',
            name='customPage',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='aiproject',
            name='homePage',
            field=models.BooleanField(),
        ),
    ]
