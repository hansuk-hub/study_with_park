# Generated by Django 3.0.7 on 2021-07-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20210718_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='', upload_to='post/%Y%m%d'),
            preserve_default=False,
        ),
    ]
