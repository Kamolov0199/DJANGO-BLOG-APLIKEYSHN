from django.shortcuts import render

def asosiy(request):
    return render(request, 'sabzi.html')

def Mevalar(request):
    return render(request, 'sabzi.html')

def Sabzilar(request):
    return render(request, 'kartoshka.html')

def sabzavotlar(request):
    return render(request, 'kiwi.html')



