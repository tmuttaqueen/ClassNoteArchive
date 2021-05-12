# Generated by Django 3.2 on 2021-05-12 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('User', 'User'), ('Privileged User', 'Privileged User')], default='User', max_length=20),
        ),
    ]
