# Generated by Django 4.1.3 on 2022-11-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-publish'], name='app1_post_publish_73aa99_idx'),
        ),
    ]
