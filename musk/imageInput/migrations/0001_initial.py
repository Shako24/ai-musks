# Generated by Django 4.1.2 on 2022-11-22 12:15

from django.db import migrations, models
import django.db.models.deletion
import imageInput.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("custom", "0007_remove_aiproject_colorscheme"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImagePage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pageType",
                    models.CharField(
                        choices=[
                            ("Home", "Home"),
                            ("About", "About"),
                            ("Contact", "Contact"),
                            ("Custom", "Custom"),
                        ],
                        max_length=15,
                    ),
                ),
                ("pageName", models.CharField(default="Custom", max_length=25)),
                (
                    "img",
                    models.ImageField(
                        default="default.jpg",
                        upload_to=imageInput.models.get_upload_path,
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="custom.aiproject",
                    ),
                ),
            ],
        ),
    ]