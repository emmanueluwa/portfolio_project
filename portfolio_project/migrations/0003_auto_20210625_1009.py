# Generated by Django 3.0.8 on 2021-06-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_project', '0002_auto_20210622_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]