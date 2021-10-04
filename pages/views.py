from django.shortcuts import render, redirect


def index(request):

    context = {
        'key': 'value',
    }
    return render(request, 'pages/index.html', context)


def about(request):

    context = {
        'key': 'value',
    }
    return render(request, 'pages/about.html', context)
