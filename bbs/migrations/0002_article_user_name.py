# Generated by Django 2.1.8 on 2021-04-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
