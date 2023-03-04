from django.shortcuts import render, redirect


def index(request):
    context = {}
    return render(request, 'index.html', context)


