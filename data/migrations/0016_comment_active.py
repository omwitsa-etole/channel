# Generated by Django 4.0.3 on 2022-04-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_remove_comment_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
