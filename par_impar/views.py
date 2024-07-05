from django.shortcuts import render

# Create your views here.
def verifica_paridade(request):
    numero = int(request.GET.get('numero',0))
    resultado = "par" if numero % 2 == 0 else "impar"
    return render(request, 'par_impar/verifica_paridade.html',{'numero': numero, 'resultado': resultado})