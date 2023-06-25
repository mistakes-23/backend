# Generated by Django 4.2.2 on 2023-06-24 17:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("processor", "0005_remove_file_preview"),
    ]

    operations = [
        migrations.AddField(
            model_name="fileimage",
            name="text",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(
                upload_to="uploads/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["pdf"]
                    )
                ],
            ),
        ),
    ]