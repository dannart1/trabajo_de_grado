import csv
from django.shortcuts import render, HttpResponse

from sensor.models import sensor



# Create your views here.
def base(request):
    return render(request, 'sensor/base.html', {})

def set_temperatura(request):
    return render(request, 'sensor/set_temperatura.html', {})

def set_humedad(request):
    return render(request, 'sensor/set_humedad.html', {})

def set_conteo(request):
    return render(request, 'sensor/set_conteo.html', {})

def set_deteccion(request):
    return render(request, 'sensor/set_deteccion.html', {})

def set_about(request):
    return render(request, 'sensor/set_about.html', {})

def set_footer(request):
    return render(request, 'sensor/set_footer.html', {})

def set_script(request):
    return render(request, 'sensor/set_script.html', {})

def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=Lectura.csv'
    
    writer = csv.writer(response)
    writer.writerow(['id', 'IDSensor', 'Fecha', 'Hora', 'Temperatura', 'Humedad'])
    
    datos = sensor.objects.all()
    
    for i in datos:
        writer.writerow([i.id, i.IDSensor, i.Fecha, i.Hora, i.Temperatura, i.Humedad])
        
    return response