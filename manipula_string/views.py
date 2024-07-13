from django.shortcuts import render

# Função que inverte as letras da palava
def inverter_palavra(palavra):
    return palavra[::-1]

# Função que conta as vogais da palavra
def contar_vogais(string):
    # define vogais
    vogais = "aeiouAEIOU"
    #Contador de vogais
    contagem = 0
    # loop para percorrer a palavra e verificar quantas vogais
    for char in string:
        if char in vogais:
            contagem += 1
    # retorna a quantidade de vogais
    return contagem

# View que utiliza a função inverter_palavra
def inverter_palavra_view(request):
    # Inicializa a variável 'resultado' como None
    resultado = None
    # Verifica se o método da requisição é POST (quando o formulário é enviado)
    if request.method == 'POST':
        # Obtém a palavra do formulário POST usando o nome do campo 'palavra'
        palavra = request.POST.get('palavra')
        # Chama a função 'inverter_palavra' para inverter a palavra e armazena o resultado
        resultado = inverter_palavra(palavra)
    # Renderiza o template 'inverter_palavra.html', passando 'resultado' para o contexto
    return render(request, 'manipula_string/inverter_palavra.html', {'resultado': resultado})


# View que utiliza a função contar_vogais
def contar_vogais_view(request):
    # zera o resultado
    resultado = None
    if request.method == 'POST':
        string = request.POST.get('string')
        resultado = contar_vogais(string)
    return render(request, 'manipula_string/contar_vogais.html', {'resultado': resultado})