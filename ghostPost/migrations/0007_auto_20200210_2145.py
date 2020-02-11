# Generated by Django 3.0.3 on 2020-02-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostPost', '0006_auto_20200210_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boastroast',
            name='boast',
        ),
        migrations.AddField(
            model_name='boastroast',
            name='boast_or_roast',
            field=models.BooleanField(choices=[(1, 'Boast'), (0, 'Roast')], default=True),
        ),
        migrations.AlterField(
            model_name='boastroast',
            name='content',
            field=models.TextField(),
        ),
    ]