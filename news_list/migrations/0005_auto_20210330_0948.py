# Generated by Django 3.1.1 on 2021-03-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_list', '0004_auto_20210330_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
