from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        phone=request.POST['phone']
        feedback = request.POST['feedback']
        print(email,name,phone,feedback)

    return render(request, 'contact.html')