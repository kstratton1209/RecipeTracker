# Generated by Django 2.2.4 on 2020-08-26 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('profpic', models.ImageField(blank=True, default=None, null=True, upload_to='forums')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.Registration')),
            ],
        ),
    ]