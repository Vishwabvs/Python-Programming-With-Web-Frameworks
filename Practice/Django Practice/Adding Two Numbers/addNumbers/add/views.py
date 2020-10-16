from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add(request):

    a = int(request.GET['num1'])
    b = int(request.GET['num2'])

    res = a+b

    return render(request, 'result.html', {'result':res})