# Generated by Django 5.1.2 on 2024-10-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customuser_phone_number_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]