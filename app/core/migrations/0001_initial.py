# Generated by Django 3.2.8 on 2021-11-01 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='uploads')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encounterDatetime', models.DateTimeField(auto_now_add=True)),
                ('encounterType_uuid', models.CharField(default='e2790f68-1d5f-11e0-b929-000c29ad1d07', max_length=255)),
                ('location_uuid', models.CharField(default='a920a302-8c66-44d4-b4c1-6e4a7c30fabc', max_length=255)),
                ('form_uuid', models.CharField(default='8377e4ff-d0fe-44a5-81c3-74c9040fd5f8', max_length=255)),
                ('synced', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='uploads')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_uuid', models.CharField(max_length=500)),
                ('person_id', models.IntegerField()),
                ('nid', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ViralLoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laboratory_id', models.CharField(blank=True, max_length=100, null=True)),
                ('sector', models.CharField(blank=True, max_length=30, null=True)),
                ('number_orig_lab', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('health_facility', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('capture_date', models.DateField(blank=True, null=True)),
                ('access_date', models.DateField(blank=True, null=True)),
                ('nid', models.CharField(blank=True, max_length=100, null=True)),
                ('viral_load', models.CharField(blank=True, max_length=100, null=True)),
                ('viral_load_qualitative', models.CharField(blank=True, max_length=100, null=True)),
                ('synced', models.BooleanField(default=False)),
                ('formatted_nid', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Viral Load',
                'verbose_name_plural': 'Viral Loads',
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obsDateTime', models.DateTimeField(auto_now_add=True)),
                ('concept', models.CharField(max_length=255)),
                ('value_numeric', models.PositiveIntegerField(blank=True, null=True)),
                ('value_coded', models.PositiveIntegerField(blank=True, null=True)),
                ('value_datetime', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(default='a920a302-8c66-44d4-b4c1-6e4a7c30fabc', max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('voided', models.BooleanField(default=False)),
                ('synced', models.BooleanField(default=False)),
                ('encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.encounter')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
            ],
        ),
        migrations.AddField(
            model_name='encounter',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient'),
        ),
    ]
