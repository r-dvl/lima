# Generated by Django 4.2.16 on 2024-11-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_article_description_alter_article_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
