from django.shortcuts import render

# Create your views here.
def inverter_palavra(palavra):
    return palavra[::-1]

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