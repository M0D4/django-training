# Generated by Django 4.1.2 on 2022-10-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='social_link',
            field=models.URLField(blank=True, max_length=300),
        ),
    ]