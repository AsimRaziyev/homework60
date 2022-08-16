# Generated by Django 4.1 on 2022-08-16 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220816_0345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthday',
        ),
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(null=True, verbose_name='О себе'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_on_github',
            field=models.URLField(null=True, verbose_name='Ссылка на GitHub'),
        ),
    ]