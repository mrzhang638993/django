from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['mrzhang'] = 'Hello mrzhang!'
    #return render(request, 'hello.html', context)
    return render(request, 'hello.html', context)
