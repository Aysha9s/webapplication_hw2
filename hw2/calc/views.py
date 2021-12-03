from django.shortcuts import render


# Create your views here.
def no_path(request):
    return render (request, "404.html") 
    
def index_view(request):
    return render (request, "index_view.html") 

def temp_calc(request):
    return render (request, "temp_calc.html") 

def conv(request,temp,type):
    temp={} 
    type={}
    t={}
    if temp== float(request.GET["numt"]) and type== request.GET["tempretur"]:   
        t["result"]= (temp*1.8)+32
    else:
        t["result"]= (temp-32)/1.8
    return render (request, "temp_result.html",context=t)
    
def area_calc(request):
    return render (request, "area_calc.html")  
def multi(request,num1,num2):
    num1={}
    num2={}
    r={}
    if num1== request.GET["width"] and num2== request.GET["height"]:
        r["result"]= num1*num2
    return render (request, "area_result.html",context=r)

def calculator(request):
     return render (request, "calculator.html") 
def apply(request,n1,n2,op):
    n1={}
    n2={}
    op=request.GET("op")
    c={}
    if n1==int(request.GET["firstnum"]) and n2==int(request.GET["secnum"])and op=="-":
        c["result"]= n1-n2
    elif n1==int(request.GET["firstnum"]) and n2==int(request.GET["secnum"])and op=="+":
         c["result"]= n1+n2
    elif n1==int(request.GET["firstnum"]) and n2==int(request.GET["secnum"])and op=="/":
         c["result"]= n1/n2
    else:
         c["result"]= n1*n2

    return render (request, "apply_calc.html", context=c)
    


