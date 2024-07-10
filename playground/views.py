from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q, F
from django.utils.crypto import get_random_string
from django.db.models import Case, When
from django.db.models import Avg, Count, Sum, Max, Min
from .models import members, User, Profile, Project, Document, Task, Comment
import datetime

def get_all_data(request):
    models = {
        'User' : User,
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
    
                    ##################### __in() #####################
    in_query = Profile.objects.filter(
        Q(id__in = [5, 6]) | Q(role__in = 'qa')
        ).values()
    context["__in"] = in_query
    
                    ##################### __icontains() #####################
    icontains_query = Comment.objects.filter(
        text__icontains = 'dkh'
    ).values()
    context["icontains_query"] = icontains_query

                    ##################### __isnull() #####################
    isNull_query = Document.objects.filter(file__isnull=False).values()
    context["isNull_query"] = isNull_query
    
                    ##################### __gte() __Lte() #####################
    gte_lte_query = Project.objects.filter(
        Q(start_date__gte='2024-01-01') & Q(end_date__lte='2024-08-31')
    ).values
    context["gte_lte_query"] = gte_lte_query

    combined_query = Profile.objects.filter(
       ( Q(id__in = [1]) & Q(contact_number__icontains='3')) | Q(role__in='developer')
    ).values()
    context["combined_query"] = combined_query

                    ##################### EXISTS() #####################
    exists_query = User.objects.filter(username='amna_ilyas').exists()
    context['exists_query'] = exists_query

                    ##################### COUNT() #####################
    count_query = User.objects.filter(email='rifaly1100@gmail.com').count()
    context['count_query'] = count_query

                    ##################### AGGREGATION(SUM) #####################    
    sum_query = Profile.objects.aggregate(Sum('id')).values()
    context['sum'] = sum_query

                    ##################### AGGREGATION(MAX) #####################
    max_query = Profile.objects.filter(role='developer').aggregate(Max('id')).values()
    context['max'] = max_query

                    ##################### AGGREGATION(COUNT) #####################
    count_agg_query = Document.objects.filter(
        Q(version='pdf') | Q(name__icontains='a')).aggregate(Count('file')).values()
    context['count_agg'] = count_agg_query
 
                    ##################### AGGREGATION(MIN) #####################   
    min_query = User.objects.aggregate(Min('id')).values()
    context['min'] = min_query

                    ##################### AGGREGATION(AVG) #####################
    avg_query = Project.objects.filter(start_date__gte='2024-01-01').aggregate( Avg('id')).values()
    context['Avg'] = avg_query

                    ##################### ANNOTATE() #####################
    annotate_query = Comment.objects.annotate(
        author_comments_count = Count('id', filter = Q(author_id__in=[5]))).values('author_id', 'author_comments_count')
    context['annotate'] = annotate_query
    
                    ##################### CASE WHEN () #####################    
    Case_query = Profile.objects.annotate(
        rank_post = Case(When(role='manager', then=1),
                         When(role='developer', then=2),
                         When(role='qa', then=3),
                         )
    ).values()
    context['Case_When'] = Case_query
    
    # select_related_query = Document.objects.select_related('project').values()
    # context['select_related'] = select_related_query
    
                    ##################### UPDATE() #####################    
    id_2 = Profile.objects.all()[2]   
    id_2.contact_number = 35467008546
    id_2.save()
    updated_data = Profile.objects.all().values()
    context['update'] = updated_data
    
                    ##################### CREATE() #####################    
    last_created = Comment.objects.create(
        text = get_random_string(length=50),
        author = User.objects.filter(username='ahmed').first(),
        created_at = datetime.datetime.now(),
        task = Task.objects.get(id=3),
        project = Project.objects.get(id=1)
    )
    last_created.save()
    create_query = Comment.objects.all().values()
    context['create'] = create_query
    
                    ##################### DELETE() #####################   
    tobe_deleted = Comment.objects.all()[4]
    tobe_deleted.delete()    
    remaining = Comment.objects.all().values()
    context['after_delete'] = remaining
    
                    ##################### CREATE_BULK() #####################
    bulk_creating = [
        Document(
            name='Docx_2', 
            description=get_random_string(length=50), 
            version='.dox', 
            project=Project.objects.get(id=2)),
        Document(
            name='Docx_3', 
            description=get_random_string(length=50), 
            version='.dox', 
            project=Project.objects.get(id=1)),
        Document(
            name='Docx_4', 
            description=get_random_string(length=50), 
            version='.pdf', 
            project=Project.objects.get(id=1)),
        ]
    Document.objects.bulk_create(bulk_creating)
    data = Document.objects.all().values()
    context['all_data'] = data

                    ##################### UPDATE_BULK() #####################
    bulk_updating = [
        Task(id=1, title=get_random_string(length=10)),
        Task(id=2, status='working'),
        Task(id=3, status='awaiting release')
        ]
    Task.objects.bulk_update(bulk_updating, ['title', 'status'])
    tasks = Task.objects.all().values()
    context['Task'] = tasks

                    ##################### GET_OR_CREATE() #####################
    User.objects.get_or_create(username='aneeqa')
    
                    ##################### UPDATE_OR_CREATE() #####################
    # username = User.objects.update_or_create(id=8, defaults={'username':'hassan'})
    
                    ##################### ORDER_BY() #####################
    order = Profile.objects.order_by('user_id').values()
    context['order_by'] = order
    
                    ##################### UNION() #####################
    query_1 = User.objects.filter(username='hassan').values()
    query_2 = User.objects.filter(id=3).values()
    union_query = query_1.union(query_2)
    context['union'] = union_query
    
                    ##################### INTERSECTION() #####################
    query_1 = Task.objects.filter(status__icontains='ing').values()
    query_2 = Task.objects.filter(status='working').values()
    intersec_query = query_1.intersection(query_2)
    context['intersection'] = intersec_query
    
                    ##################### F() #####################
    id_3 = Profile.objects.all()[2]
    id_3.user_id = F('user_id') + 2
    id_3.save()
    
    
    
                    
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
