from django.contrib import admin

from core.models import CsvFile, ExcelFile, Patient, ViralLoad, Encounter, Observation, ExcelImport


class ViraLoadAdmin(admin.ModelAdmin):
    ordering = ['patient_name']
    list_display = [
        'patient_name', 'nid', 'formatted_nid', 'viral_load', 'viral_load_qualitative', 'capture_date'
    ]
    list_filter = ('viral_load_qualitative',)


class ExcelImportAdmin(admin.ModelAdmin):
    ordering = ['patient_name']
    list_display = [
        'patient_name', 'nid', 'viral_load', 'viral_load_qualitative', 'capture_date'
    ]
    list_filter = ('viral_load_qualitative',)


admin.site.register(CsvFile)
admin.site.register(ExcelFile)
admin.site.register(ViralLoad, ViraLoadAdmin)
admin.site.register(Patient)
admin.site.register(Encounter)
admin.site.register(Observation)
admin.site.register(ExcelImport, ExcelImportAdmin)
