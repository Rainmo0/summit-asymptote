from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495722',
        'name': 'Farras Syafiq U',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)