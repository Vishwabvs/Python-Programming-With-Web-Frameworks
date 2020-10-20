from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add(request):

    a = int(request.POST['num1'])
    b = int(request.POST['num2'])

    #If we want to use using GET method replace POST keyword with GET...

    res = a+b

    return render(request, 'result.html', {'result':res})