from django.shortcuts import render

def anasayfa(request):
    context = {
        'isim': 'og celik'
    }
    return render(request, 'pages/anasayfa.html', context=context)