from django.shortcuts import render
from django.http import HttpResponse
import math as m
def home(request):
    return render(request,'home.html')
# Create your views here.
def solution(request):
    try:
        val1 = request.POST.get('num1', False)
        val2 = request.POST.get('num2', False)
        val3 = request.POST.get('num3', False)
        request.POST.get('submit', False)
        if request.POST.get('add', False) == 'ADD':
            return render(request, "home.html", {'res': "The result is %.3f"%(float(val1) + float(val2))})
        elif request.POST.get('subtract', False) == 'SUBTRACT':
            return render(request, "home.html", {'res': "The result is %.2f"%(float(val1) - float(val2))})
        elif request.POST.get('multiply', False) == 'MULTIPLY':
            return render(request, "home.html", {'res': "The result is %.2f"%(float(val1) * float(val2))})
        elif request.POST.get('divide', False) == 'DIVIDE':
            return render(request, "home.html", {'res': "The result is %.4f"%(float(val1) / float(val2))})
        elif request.POST.get('root', False) == 'SQA. ROOT':
            return render(request, "home.html", {'res': "The Square Root is %.2f"%(m.sqrt(float(val3)))})
        elif request.POST.get('pow', False) == 'POWER':
            return render(request, "home.html", {'res': "The result is %.2f"%(m.pow(float(val1),float(val2)))})
        elif request.POST.get('nroot', False) == 'Nth ROOT':
            return render(request, "home.html", {'res': "The %d root of %d is %.2f"%(int(val1),int(val2),m.ceil(float(val1)**(1/int(val2))))})
        elif request.POST.get('fact', False) == 'FACTORIAL':
            return render(request, "home.html", {'res': "The Factorial is %d"%(m.factorial(int(val3)))})
        elif request.POST.get('gcd', False) == 'GCD':
            return render(request, "home.html", {'res': "The GCD of %d and %d is %d"%(val1,val2,m.gcd(int(val1),int(val2)))})
        elif request.POST.get('conv', False) == 'Number system Conversion':
            return render(request, "home.html", {'res': "Binary: {}  Octal: {}  Hexadecimal: {}".format(str(bin(int(val3)))[2::],str(oct(int(val3)))[2::],str(hex(int(val3)))[2::]).upper()})
        elif request.POST.get('rem', False) == 'Remainder':
            return render(request, "home.html", {'res': "The Remainder is %d"%(m.remainder(int(val1),int(val2)))})
        elif request.POST.get('sin', False) == 'SIN':
            return render(request, "home.html", {'res': "Sin(%d) = %.4f"%(int(val3),m.sin(int(val3)))})
        elif request.POST.get('cos', False) == 'COS':
            return render(request, "home.html", {'res': "Cos(%d) = %.4f"%(int(val3),m.cos(int(val3)))})
        elif request.POST.get('tan', False) == 'TAN':
            return render(request, "home.html", {'res': "Tan(%d) = %.4f"%(int(val3),m.tan(int(val3)))})
        elif request.POST.get('log10', False) == 'LOG10':
            return render(request, "home.html", {'res': "Log10(%f) = %.4f"%(float(val3),m.log10(float(val3)))})
        elif request.POST.get('log', False) == 'LOG':
            return render(request, "home.html", {'res': "Log(%f) = %.4f"%(float(val3),m.log(float(val3)))})
        elif request.POST.get('evaluate', False) == 'Evaluate':
            return render(request, "home.html", {'res': "The result of the expression is %.2f"%(eval(str(val3)))})
        elif request.POST.get('hyp', False) == 'Hypotenuse':
            return render(request, "home.html", {'res': "The hypotenuse is %.2f"%(m.hypot(float(val1),float(val2)))})
        elif request.POST.get('isprime', False) == 'Is Prime?':
            if int(val3)> 1:
                for i in range(2, (int(val3) // 2)+1):
                    if (int(val3) % i) == 0:
                        return render(request, "home.html" , {'res': "%d is not a prime number"%(int(val3))})
                        break
                else:
                    return render(request, "home.html", {'res': "%d is a prime number" % (int(val3))})
            else:
                return render(request, "home.html", {'res': "%d is not a prime number" % (int(val3))})
        elif request.POST.get('exp', False) == 'e^n':
            return render(request, "home.html", {'res': "e^%.2f= %.4f"%(float(val3),m.exp(float(val3)))})

    except Exception:
        return render(request, "home.html", {'res': "Invalid inputs entered"})