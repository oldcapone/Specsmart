# Generated by Django 4.1.3 on 2022-11-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_tag_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_detail',
            field=models.TextField(blank=True),
        ),
    ]