# Generated by Django 5.1.2 on 2024-12-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libManagement', '0006_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$2mJzaz6nZKcl7u01teLhwv$ZdPRoBVx7tBE3RmbFV24FQA168O7qw5ewDkOgrmUB5M=', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='pbkdf2_sha256$870000$3H3m0nttDnIcZUMaVTmG0u$kWwkF4A7pLgdP/kyjBu9KocoY7vW8wh1pfIndy6fLtI=', max_length=100, unique=True),
        ),
    ]
