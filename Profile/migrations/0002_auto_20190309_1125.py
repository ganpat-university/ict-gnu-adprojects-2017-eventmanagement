# Generated by Django 2.1.7 on 2019-03-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='ProfilePics'),
        ),
    ]
