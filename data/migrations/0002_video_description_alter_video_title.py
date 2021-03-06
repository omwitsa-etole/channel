# Generated by Django 4.0.3 on 2022-04-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.CharField(blank=True, help_text='Video Description', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(help_text='Enter Video Title', max_length=100),
        ),
    ]
