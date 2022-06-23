# Generated by Django 4.0.4 on 2022-06-06 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0053_remove_agenthistory_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='goarch',
            field=models.CharField(blank=True, choices=[('amd64', 'amd64'), ('386', '386'), ('arm64', 'arm64'), ('arm', 'arm')], max_length=255, null=True),
        ),
    ]