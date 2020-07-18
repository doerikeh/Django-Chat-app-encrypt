# Generated by Django 3.0.2 on 2020-03-21 18:11

from django.db import migrations
import django_cryptography.fields
import mirage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200321_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='body',
            field=django_cryptography.fields.encrypt(mirage.fields.EncryptedTextField(unique=True)),
        ),
    ]
