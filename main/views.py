from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Anastasia Keisha Bella Arianne Pepe',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)