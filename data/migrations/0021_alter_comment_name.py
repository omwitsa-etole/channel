# Generated by Django 4.0.3 on 2022-04-03 19:14

import data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default=data.models.User, max_length=100),
        ),
    ]
