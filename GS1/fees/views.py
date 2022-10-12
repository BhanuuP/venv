from django.shortcuts import render

def fees_django(request):
    return render(request, 'fees/fees1.html',{'cname':'django','cfees':'5500'})
