# Generated by Django 3.2.19 on 2023-06-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cure',
            name='disease_description',
            field=models.TextField(default='Disease description'),
            preserve_default=False,
        ),
    ]