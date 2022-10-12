from django.shortcuts import render

def learn_django(request):
    return render(request, 'course/course1.html',{'cname':'django'})
