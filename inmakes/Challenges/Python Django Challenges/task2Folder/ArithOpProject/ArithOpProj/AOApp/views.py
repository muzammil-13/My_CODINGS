from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def result(request):
    return render(request, "result.html")


def addition(request):
    x = int(request.GET['add1'])
    y = int(request.GET['add2'])
    res1 = x + y
    return render(request, "result.html", {'res1': res1})


def subtraction(request):
    q = int(request.GET['sub1'])
    w = int(request.GET['sub2'])
    res2 = q - w
    return render(request, "result.html", {'res2': res2})


def multiplication(request):
    a = int(request.GET['mul1'])
    s = int(request.GET['mul2'])
    res3 = a * s
    return render(request, "result.html", {'res3': res3})


def division(request):
    z = int(request.GET['div1'])
    c = int(request.GET['div2'])
    res4 = z / c
    return render(request, "result.html", {'res4': res4})
