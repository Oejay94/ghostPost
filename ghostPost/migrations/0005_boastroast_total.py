# Generated by Django 3.0.3 on 2020-02-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostPost', '0004_auto_20200210_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='boastroast',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
