# Generated by Django 2.2.18 on 2021-02-17 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workCk', '0003_auto_20210218_0755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='author',
        ),
        migrations.AddField(
            model_name='work',
            name='work_Nmae',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
