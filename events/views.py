from django.shortcuts import render,redirect
from django.http import HttpResponse
from events.form import EventModelForm,CategoryModelForm,ParticipantModelForm
from events.models import Event,Category,Participant
from django.contrib import messages
from datetime import date
from django.db.models import Q,Count
def main_dashboard(request,):
    
    counts=Event.objects.aggregate(
        total_event=Count('id'),
        today_event=Count('id',filter=Q(date= date.today())),
        upcoming_event=Count('id',filter=Q(date__gte=date.today())),
        past_event=Count('id',filter=Q(date__lt=date.today()))
    )
    category=Category.objects.all()
    
    total_participants =Participant.objects.values('name').distinct().count()

    type=request.GET.get("type","all")
    base_quary=Event.objects.select_related('category').prefetch_related("event_participant")
    
    if type=='today_event':
        events=base_quary.filter(date=date.today())
    elif type=='upcoming_event':
        events=base_quary.filter(date__gte=date.today())
    elif type=='past_event':
        events=base_quary.filter(date__lt=date.today())
    elif type=='all':
        events=base_quary.all()
        
    category_id=request.GET.get("category")
    if category_id:
        events=base_quary.filter(category_id=category_id)
    
    search_item=request.GET.get("search")
    
    if search_item:
        events=Event.objects.filter(Q(name__icontains=search_item)|Q(location__icontains=search_item))
        
    
    
    context={
        'count':counts,
        'all_category':category,
        'participant':total_participants,
        'events':events
    }

    return render(request,'dashboard.html',context)

def detail(request,id):
    
    event=Event.objects.get(id=id)
 
    event_participant= event.event_participant.all()
    context={'event':event,'event_participant':event_participant}
    return render(request,'detail.html',context)

def creat_event(request):
    event_form=EventModelForm()
    
    if request.method=="POST":
        event_form=EventModelForm(request.POST)
        
        if event_form.is_valid():
            event_form.save()
            messages.success(request,"Event Creat Successfully")
            return redirect("create_event")
    context={"event_form":event_form}
    return render(request,'event_form.html',context)

def event_category(request):
    
    category_event=CategoryModelForm()
    if request.method=="POST":
        category_event=CategoryModelForm(request.POST)
        if category_event.is_valid():
            category_event.save()
    context={"category_event":category_event}
    return render(request,'category.html',context)

def delete_category(request,id):
    if request.method=='POST':
        category=Category.objects.get(id=id)
        category.delete()
        return redirect("main_dashboard")

def update_category(request,id):
    category=Category.objects.get(id=id)
    category_event=CategoryModelForm(instance=category)
    if request.method=='POST':
        category_event=CategoryModelForm(request.POST,instance=category)
        if category_event.is_valid():
            category_event.save()
            messages.success(request,"Category Update succesfully")
            return redirect('update_category',id)
    context={'category_event':category_event}
    return render(request,'category.html',context)

def event_participant(request):
    participant=ParticipantModelForm()
    if request.method=="POST":
        participant=ParticipantModelForm(request.POST)
        if participant.is_valid():
            participant.save()
    context={"participant":participant}
    return render(request,'participant.html',context)


def delete_participant(request,id):
    
    if request.method=='POST':
        participant=Participant.objects.get(id=id)
        participant.delete()
        return redirect("main_dashboard")
        
    else:
        messages.success(request,'somting went wrong')
        return redirect("main_dashboard")
    
def update_participant(request,id):
    participant_event=Participant.objects.get(id=id)
    participant=ParticipantModelForm(instance=participant_event)
    if request.method=='POST':
        participant=ParticipantModelForm(request.POST,instance=participant_event)
        if participant.is_valid():
            participant.save()
    context={"participant":participant}
    return render(request,'participant.html',context)
    
    

def event_delete(request,id):
    if request.method=='POST':
        event=Event.objects.get(id=id)
        event.delete()
        return redirect("main_dashboard")
        
    else:
        messages.success(request,'somting went wrong')
        return redirect("main_dashboard")


def event_update(request,id):
    event=Event.objects.get(id=id)
    event_form=EventModelForm(instance=event)
    if request.method=='POST':
        event_form=EventModelForm(request.POST,instance=event)
        if event_form.is_valid():
            event_form.save()
            messages.success(request,"Event Update succesfully")
            return redirect('update_event',id)
    
    
    context={"event_form":event_form}
    return render(request,"event_form.html",context)




    
    