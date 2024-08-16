from django.shortcuts import render
import datetime

# Create your views here.

def filters(request):
    date=datetime.datetime.now
    d={'data':"tHiS iS aN eXaMpLe To UnDeRsTaNd FiLtErS",'c':1,"e":1000,"date":date,"f":1}
    return render(request,"filters.html",d)

def usd_filters(request):
    d={'data':'tHiS iS aN eXaMpLe To UnDeRsTaNd UsErDeFiNeD FiLtErS'}
    return render(request,"usd_filters.html",d)