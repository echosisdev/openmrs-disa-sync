# Generated by Django 3.2.8 on 2021-10-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_viralload_viral_load'),
    ]

    operations = [
        migrations.AddField(
            model_name='viralload',
            name='formatted_nid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
