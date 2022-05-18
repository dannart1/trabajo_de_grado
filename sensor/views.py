from django.shortcuts import render, HttpResponse



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
