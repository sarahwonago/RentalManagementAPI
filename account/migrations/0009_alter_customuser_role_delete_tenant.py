# Generated by Django 5.1.2 on 2024-10-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_tenant_landlord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('landlord', 'landlord'), ('tenant', 'tenant'), ('superadmin', 'superadmin')], help_text="Role either: 'superadmin','landlord' or 'tenant'.", max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
    ]
