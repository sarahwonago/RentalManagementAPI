# Generated by Django 5.1.2 on 2024-10-23 08:59

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('landlord', 'landlord'), ('tenant', 'tenant'), ('superadmin', 'superadmin')], help_text="Role either: 'user','landlord' or 'tenant'.", max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('landlord', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='landlordtenants', to=settings.AUTH_USER_MODEL)),
                ('tenant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]