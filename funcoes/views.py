from django.shortcuts import render

# Create your views here.
def somar_lista(numeros):
    return sum(numeros)

# View que utiliza a função

def somar_numeros_view(request):
    if request.method == 'POST':
        numeros_str = request.POST.get('numeros')
        numeros = list(map(int, numeros_str.split(',')))
        resultado = somar_lista(numeros)
        return render(request, 'funcoes/somar_numeros.html', {'resultado': resultado})
    return render(request, 'funcoes/somar_numeros.html')