# Generated by Django 3.2.15 on 2022-09-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_socialnetworkuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetworkuser',
            name='followers',
            field=models.ManyToManyField(to='core.SocialNetworkUser'),
        ),
    ]