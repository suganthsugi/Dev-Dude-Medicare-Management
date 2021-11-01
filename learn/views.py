from django.shortcuts import render

# Create your views here.
def python(request):
    return render(request, 'python.html')

def python1_print(request):
    return render(request, 'python1_print.html')