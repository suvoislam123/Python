# Generated by Django 4.0.3 on 2022-04-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
