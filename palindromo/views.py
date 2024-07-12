from django.shortcuts import render

# Função que identifica se a palavra é um palindromo
def identifica_palindromo(palavra):
    # palavra[::-1] é uma técnica de slicing que inverte a string. A função verifica se a palavra é igual à sua versão invertida.
    return palavra == palavra[::-1]

# view para utilizar a função que identifica se é palindromo
def verificar_palindromo_view(request):
    # Inicia a variave 'resultado' como None
    resultado = None
    #Verifica se o método da requisição é POST  (quando o formulário é enviado)
    if request.method == 'POST':
        palavra = request.POST.get('palavra')
        resultado = identifica_palindromo(palavra)
    return render(request, 'palindromo/verificar_palindromo.html', {'resultado': resultado})