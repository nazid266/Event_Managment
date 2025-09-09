from django.shortcuts import render,redirect
from django.http import HttpResponse
from events.form import EventModelForm,CategoryModelForm
from events.models import Event,Category
from django.contrib import messages
from datetime import date
from django.db.models import Q,Count
from django.contrib.auth.decorators import user_passes_test
from event_users.views import is_admin


def is_organizer(user):
    return user.groups.filter(name="Organizer")

def is_perticipant(user):
    return user.groups.filter(name="Participant")

@user_passes_test(is_organizer,login_url="no_permission")
def main_dashboard(request):
    
    counts=Event.objects.aggregate(
        total_event=Count('id'),
        today_event=Count('id',filter=Q(date= date.today())),
        upcoming_event=Count('id',filter=Q(date__gte=date.today())),
        past_event=Count('id',filter=Q(date__lt=date.today()))
    )
    category=Category.objects.all()
    
    total_participants =Event.objects.aggregate(total=Count('Participants', distinct=True))['total']

    type=request.GET.get("type","all")
    base_quary=Event.objects.select_related('category').prefetch_related("Participants")
    
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
 
    event_participant= event.Participants.all()
    context={'event':event,'event_participant':event_participant}
    return render(request,'detail.html',context)

@user_passes_test(is_organizer,login_url="no_permission")
def creat_event(request):
    event_form=EventModelForm()
    
    if request.method=="POST":
        event_form=EventModelForm(request.POST,request.FILES)
        
        if event_form.is_valid():
            event_form.save()
            messages.success(request,"Event Creat Successfully")
            return redirect("create_event")
        else:
            print(event_form.errors)
    context={"event_form":event_form}
    return render(request,'event_form.html',context)

@user_passes_test(is_organizer,login_url="no_permission")
def event_category(request):
    
    category_event=CategoryModelForm()
    if request.method=="POST":
        category_event=CategoryModelForm(request.POST)
        if category_event.is_valid():
            category_event.save()
    context={"category_event":category_event}
    return render(request,'category.html',context)



@user_passes_test(is_organizer,login_url="no_permission")
def delete_category(request,id):
    if request.method=='POST':
        category=Category.objects.get(id=id)
        category.delete()
        return redirect("main_dashboard")


@user_passes_test(is_organizer,login_url="no_permission")
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


@user_passes_test(is_perticipant,login_url="no_permission")
def rsvp_event(request,id):
    event=Event.objects.get(id=id)
    if request.user in event.Participants.all():
        messages.success(request,f"You have rsvped  {event.name} event")
    else:
        event.Participants.add(request.user)
        messages.success(request,f"You sucessfully rsvped  {event.name}  event")
        
    return redirect("participant_dashboard")

    

    
@user_passes_test(is_perticipant,login_url="no_permission")    
def participant_dashboard(request):
    counts=Event.objects.aggregate(
        today_event=Count('id',filter=Q(date=date.today())),
        upcoming_event=Count('id',filter=Q(date__gte=date.today())),
        past_event=Count('id',filter=Q(date__lt=date.today())),
    )
    
    rsvp_event_count=request.user.rsvp_events.count()
    
    type=request.GET.get("type","all")
    base_query=Event.objects.select_related('category').prefetch_related("Participants")
    
    if type=="today_event":
        events=base_query.filter(date=date.today())
    elif type=="upcoming_event":
        events=base_query.filter(date__gte=date.today())
    elif type=="past_event":
        events=base_query.filter(date__lt=date.today())
    elif type=="all":
        events=request.user.rsvp_events.all()
        
    search_item=request.GET.get("search")
    if search_item:
        events=Event.objects.filter(Q(name__icontains=search_item)|Q(location__icontains=search_item))
    category=Category.objects.all()
    
    select_category_id=request.GET.get("category")
    if select_category_id:
        events=base_query.filter(category_id=select_category_id)
    
    context={'counts':counts,'rsvp_event_count':rsvp_event_count,'events':events,'all_category':category}
    return render(request,'participant_dashboard.html',context)




@user_passes_test(is_organizer,login_url="no_permission")
def event_delete(request,id):
    if request.method=='POST':
        event=Event.objects.get(id=id)
        event.delete()
        return redirect("main_dashboard")
        
    else:
        messages.success(request,'somting went wrong')
        return redirect("main_dashboard")



@user_passes_test(is_organizer,login_url="no_permission")
def event_update(request,id):
    event=Event.objects.get(id=id)
    event_form=EventModelForm(instance=event)
    if request.method=='POST':
        event_form=EventModelForm(request.POST,request.FILES,instance=event)
        if event_form.is_valid():
            event_form.save()
            messages.success(request,"Event Update succesfully")
            return redirect('update_event',id)
    
    
    context={"event_form":event_form}
    return render(request,"event_form.html",context)



def dashboar(request):
    if is_admin(request.user):
        return redirect("admin_dashboard")
    elif is_organizer(request.user):
        return redirect("main_dashboard")
    elif is_perticipant(request.user):
        return redirect("participant_dashboard")
   
    return redirect("no_permission")



    
    