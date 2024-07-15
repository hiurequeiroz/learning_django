from django.shortcuts import render
from collections import Counter

# função que ordena numeros
def ordenar_numeros(numeros):
    numeros = [int(numero) for numero in numeros]
    numeros.sort()
    return numeros

def contar_palavras(frase):
    palavras = frase.split()

    frequencia = Counter(palavras)
    return frequencia

# view que recebe as informações do formulário e utilzia a função que ordena os numeros e devolve 
def ordenar_numeros_view(request):
    resultado = None
    if request.method == 'POST':
        numeros = request.POST.get('numeros').split(',')
        resultado = ordenar_numeros(numeros)
    return render(request, 'lista_dicionario/ordenar_numeros.html', {'resultado': resultado})

def contar_palavras_view(request):
    resultado = None
    if request.method == 'POST':
        frase = request.POST.get('frase')
        resultado = contar_palavras(frase)
    return render(request, 'lista_dicionario/contar_palavras.html', {'resultado': resultado})