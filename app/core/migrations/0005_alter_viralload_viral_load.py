# Generated by Django 3.2.8 on 2021-10-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_viralload_laboratory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viralload',
            name='viral_load',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
