# Generated by Django 4.0.3 on 2022-04-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0028_remove_comment_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='User', max_length=100, null=True),
        ),
    ]
