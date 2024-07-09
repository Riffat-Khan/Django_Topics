from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import members, Profile, Project, Document, Task, Comment

def get_all_data(request):
    models = {
        'Profile': Profile, 
        'Project': Project, 
        'Task': Task, 
        'Document': Document, 
        'Comment': Comment
        }
    
    context = {}
    for model_name, model in models.items():
        getting_data = model.objects.all().values()
        context[model_name] = list(getting_data)
        
    return render(request, 'template.html', {'context': context})

def queries(request):
    obj = Q()
    context = {}
    in_query = Profile.objects.filter(
        Q(id__in = [5, 6]) | Q(role__in = 'qa')
        ).values()
    context["__in"] = in_query
    
    icontains_query = Comment.objects.filter(
        text__icontains = 'dkh'
    ).values()
    context["icontains_query"] = icontains_query
    
    isNull_query = Document.objects.filter(file__isnull=False).values()
    context["isNull_query"] = isNull_query
    
    gte_lte_query = Project.objects.filter(
        Q(start_date__gte='2024-01-01') & Q(end_date__lte='2024-08-31')
    ).values
    context["gte_lte_query"] = gte_lte_query
    
    combined_query = Profile.objects.filter(
       ( Q(id__in = [1]) & Q(contact_number__icontains='3')) | Q(role__in='developer')
    ).values()
    context["combined_query"] = combined_query
    
    return render(request, 'template.html', {'context' : context})


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
