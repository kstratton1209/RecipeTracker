# Generated by Django 2.2.4 on 2020-07-31 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20200728_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='img',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
