# Generated by Django 5.1.2 on 2024-12-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libManagement', '0005_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$HubzIz4HGElktNBRdeHrTF$7lkAxUeZGfek4vgC3Vft2otvxgGJKN/vwGMNfv0SHYE=', max_length=100),
        ),
    ]
