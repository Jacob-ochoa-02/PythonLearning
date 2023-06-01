from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from .models import Product

# Create your views here.

# /productos


def index(request):
    # return HttpResponse('Hola mundo!')
    # Permite buscar todos los registros en nuestra BD
    products = Product.objects.all()  # Don't need values without JsonResponse

    return render(request, 'index.html', context={'productos': products})
    # print(products)
    # return JsonResponse(list(products), safe=False) # add 1st line  to use it
    # products = Product.objects.filter(puntaje=3)
    # products = Product.objects.get(id=1)    # id o pk
    # puntaje__gte greater than or equal = #n -> numero
    # puntaje__gt greater than #n -> numero
    # puntaje__lte less than or equal than = #n -> numero
    # puntaje__lt less than #n -> numero
    # Permite que nuestras consultas sean un poco más complejas


def detalle(request, producto_id):
    # return HttpResponse(producto_id)
    # try:
    # producto = Product.objects.get(id=producto_id)
    producto = get_object_or_404(Product, id=producto_id)
    return render(
        request, 'detalle.html',
        context={'producto': producto})
    # except Product.DoesNotExist:
    #     raise Http404()


def formulario(request):
    if request.method == 'POST':
        # Se crea el formulario si el metodo es "Post"
        # Se guardan todos los valores en la propiedad de POST
        form = ProductForm(request.POST)
        if form.is_valid():
            # En el caso de que el formulario sea valido se inserta en la base de datos
            form.save()
            # Toma el usuario y lo redirige al listado de productos
            return HttpResponseRedirect('/productos')
    else:
        form = ProductForm()
    # form = ProductForm()
    return render(request, 'producto_form.html', context={'form': form})
