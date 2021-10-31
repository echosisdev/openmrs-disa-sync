from django.shortcuts import render
from core.forms import ExcelForm
from core.models import CsvFile, ExcelFile, ViralLoad, ExcelImport
from core.utils.data_convertion import DataConversion


import csv
import pandas as pd


#  0 laboratory_id = models.IntegerField(null=True, blank=True)
#  5   sector = models.CharField(max_length=30, blank=True, null=True)
#  7  number_orig_lab = models.CharField(max_length=100, blank=True, null=True)
#  9   province = models.CharField(max_length=100, blank=True, null=True)
#  11   district = models.CharField(max_length=100, blank=True, null=True)
#  12  health_facility = models.CharField(max_length=100, blank=True, null=True)
#  14   patient_name = models.CharField(max_length=100, blank=True, null=True)
#  22   gender = models.CharField(max_length=100, blank=True, null=True)
#  23   reference = models.CharField(max_length=100, blank=True, null=True)
#  32   capture_date = models.DateField(null=True, blank=True)
#  34   access_date = models.DateField(null=True, blank=True)
#  41   nid = models.CharField(max_length=100, blank=True, null=True)
#  56   viral_load = models.PositiveIntegerField(null=True, blank=True)
#  58   viral_load_qualitative = models.CharField(
#         max_length=100, blank=True, null=True)

def upload_excel_file(request):
    form = ExcelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ExcelForm()
        excel_file = ExcelFile.objects.get(activated=False)
        with open(excel_file.file_name.path, 'rb') as file:
            df = pd.read_excel(
                file, sheet_name='Resultados da Análise', skiprows=[0, 1, 2])
            df.to_csv(r'laboratorio.csv', index=None,
                      header=True, encoding='utf-8')
            excel_file.activated = True
            excel_file.save()

        with open('laboratorio.csv', 'r') as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                if str(row[56]).startswith('<'):
                    viral_load_data = ''
                    viral_load_qualitative_data = row[56]
                elif str(row[56]) is None:
                    viral_load_qualitative_data = row[58]
                else:
                    viral_load_data = row[56]
                    viral_load_qualitative_data = row[58]
                viralLoad = ViralLoad.objects.create(
                    laboratory_id=row[0],
                    sector=row[5],
                    number_orig_lab=row[7],
                    province=row[9],
                    district=row[11],
                    health_facility=row[12],
                    patient_name=row[14],
                    gender=row[22],
                    reference=row[23],
                    capture_date=DataConversion.convert_to_datetime(
                        str(row[32])),
                    access_date=DataConversion.convert_to_datetime(
                        str(row[34])),
                    nid=DataConversion.format_nid(str(row[41])),
                    viral_load=viral_load_data,
                    viral_load_qualitative=viral_load_qualitative_data
                )
                viralLoad.save()
                ViralLoad.objects.filter(nid="").delete()
                ViralLoad.objects.filter(viral_load__contains="NAME").delete()
                # qs = ExcelImport.objects.all()
                # for q in qs:
                #     viral_load = ViralLoad.objects.create(
                #         laboratory_id=q.laboratory_id,
                #         sector=q.sector,
                #         number_orig_lab=q.laboratory_id,
                #         province=q.province,
                #         district=q.district,
                #         health_facility=q.health_facility,
                #         patient_name=q.patient_name,
                #         gender=q.gender,
                #         reference=q.reference,
                #         capture_date=q.capture_date,
                #         access_date=q.access_date,
                #         nid=DataConversion.format_nid(q.nid),
                #         viral_load=q.viral_load,
                #         viral_load_qualitative=q.viral_load_qualitative
                #     )
                #     viral_load.save()
   # ExcelImport.objects.all().delete()

    return render(request, 'app/upload.html', {'form': form})
