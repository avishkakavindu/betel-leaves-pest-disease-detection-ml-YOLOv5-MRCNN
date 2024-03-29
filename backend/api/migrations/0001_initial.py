# Generated by Django 3.2.19 on 2023-06-03 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_or_pest', models.CharField(choices=[('bacterial_leaf_blight', 'Bacteria Leaf Blight'), ('leaf_spot', 'Leaf Spot'), ('stem_disease', 'Stem Disease'), ('mealybug', 'Mealy Bug'), ('whitefly', 'White Fly')], max_length=255)),
                ('cure_description', models.TextField()),
                ('type', models.CharField(choices=[('pest', 'Pest'), ('disease', 'Disease')], default='disease', max_length=20)),
            ],
        ),
    ]
