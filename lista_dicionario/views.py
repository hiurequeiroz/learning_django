from django.shortcuts import render

# função que ordena numeros
def ordenar_numeros(numeros):
    numeros = [int(numero) for numero in numeros]
    numeros.sort()
    return numeros

def ordenar_numeros_view(request):
    resultado = None
    if request.method == 'POST':
        numeros = request.POST.get('numeros').split(',')
        resultado = ordenar_numeros(numeros)
    return render(request, 'lista_dicionario/ordenar_numeros.html', {'resultado': resultado})