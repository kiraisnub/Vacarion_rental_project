# Generated by Django 5.0.3 on 2024-06-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0005_alter_customhostuser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customhostuser',
            name='Profile',
            field=models.ImageField(upload_to='pro_pics'),
        ),
    ]
