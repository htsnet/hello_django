from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello<h1>')


def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))


def soma(request, num1, num2):
    soma = num1 + num2
    return HttpResponse('<h1>A soma de {} com {} é {}<h1>'.format(num1, num2, soma))


def subtracao(request, num1, num2):
    subtracao = num1 - num2
    return HttpResponse('<h1>A subtração de {} por {} é {}<h1>'.format(num1, num2, subtracao))


def multiplicacao(request, num1, num2):
    resultado = num1 * num2
    return HttpResponse('<h1>A multiplicação de {} com {} é {}<h1>'.format(num1, num2, resultado))


def divisao(request, num1, num2):
    if num2 != 0:
        resultado = num1 / num2
        texto = '<h1>A divisao de {} por {} é {}<h1>'.format(num1, num2, resultado)
    else:
        texto = "<h1>Não é possível dividir por zero</h1>"
    return HttpResponse(texto)