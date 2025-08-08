from django.shortcuts import render

def home(request):
    context = {
        "my_name": "Alisher"
    }
    return render(request, 'index.html', context)
