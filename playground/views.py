from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import members

def site(request):
    return render(request, 'home.html')
    template = loader.get_template('hello.html')
    return HttpResponse(template.render(request))

def member(request):
    # member = members.objects.all().values()
    member = members.objects.filter(lastname = 'ali').values()
    context = {
        'member' : member
    }
    template = loader.get_template('all_members.html')
    return HttpResponse(template.render(context, request))

def details(request, id):
    # member = members.objects.get(id=id)
    member = get_object_or_404(members, id=id)
    context = {
        'member' : member
    }
    template = loader.get_template('details.html')
    return HttpResponse(template.render(context, request))
