# Generated by Django 3.0.3 on 2020-02-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostPost', '0002_auto_20200210_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boastroast',
            name='boast',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='boastroast',
            name='roast',
            field=models.BooleanField(default=False),
        ),
    ]