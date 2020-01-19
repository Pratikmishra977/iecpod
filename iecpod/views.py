from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'index':'active'})

def contact(request):
    return render(request, 'contactUs.html', {'contact': 'active'})