# Generated by Django 3.0.7 on 2020-06-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200606_0103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст отзыва'),
        ),
    ]
