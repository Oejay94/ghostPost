# Generated by Django 3.0.3 on 2020-02-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostPost', '0005_boastroast_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boastroast',
            name='boast',
            field=models.BooleanField(choices=[(1, 'Boast'), (2, 'Roast')], default=True),
        ),
    ]
