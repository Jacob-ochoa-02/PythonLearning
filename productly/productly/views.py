from django.shortcuts import render # Se usa para devolver codigo html al usuario

def inicio(request):
    return render(
        request,
        'inicio.html'
    )