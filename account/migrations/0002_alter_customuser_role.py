# Generated by Django 5.1.2 on 2024-10-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('landlord', 'landlord'), ('tenant', 'tenant')], default='tenant', help_text="Role of the user, either 'landlord' or 'tenant'.", max_length=10),
        ),
    ]