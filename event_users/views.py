from django.shortcuts import render,redirect,HttpResponse
from event_users.form import RegistationForm,loginForm,Assing_role,Create_group_Form
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User,Group
from django.db.models import Prefetch,Q,Count
from django.contrib.auth.decorators import user_passes_test,login_required

# Create your views here.


def is_admin(user):
    return user.groups.filter(name="Admin").exists()





def sing_up(request):
    if request.method=='GET':
        form=RegistationForm() 
        
    if request.method=='POST':
        form=RegistationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.is_active=False
            user.save()
            messages.success(request,"Your Conformation Email Sent....Please Check This Email")
            return redirect('sing_in')
   
    
         
            
    return render(request,'registration/sing_up.html',{"form":form})
    

def sing_in(request):
    if request.method=='GET':
        form=loginForm()
    if request.method=='POST':
        form=loginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
            
    return render(request,"registration/sing_in.html",{"form":form})

@login_required
def sing_out(request):
        logout(request)
        return redirect('sing_in')
        
 
 
def activate_user(request,user_id,token):
    try:
        user=User.objects.get(id=user_id)
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            return redirect('sing_in')
        else:
            return HttpResponse('Invalid Id Or Token')
        
    except User.DoesNotExist:
        return HttpResponse('User Not Found')    


@user_passes_test(is_admin,login_url="no_permission")
def role_assign(request,id):
    user=User.objects.get(id=id)
    form=Assing_role()
    if request.method=="POST":
        form=Assing_role(request.POST)
        if form.is_valid():
            role=form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request,f"{user.username} Has Assigned The {role.name} Role")
            return redirect("assign_role",id=id)
            
    return render(request,"admin/assign_role.html",{"form":form})
  
          

@user_passes_test(is_admin,login_url="no_permission")     
def create_group(request):
    form=Create_group_Form()
    if request.method=="POST":
        form=Create_group_Form(request.POST)
        if form.is_valid():
            group=form.save()
            messages.success(request,f"{group.name} successfully created")
            return redirect("create_group")
    return render(request,"admin/create_group.html",{"form":form})



@user_passes_test(is_admin,login_url="no_permission")
def group_list(request):
    groups=Group.objects.prefetch_related("permissions").all()
    return render(request,"admin/group_list.html",{"groups":groups})



@user_passes_test(is_admin,login_url="no_permission")
def admin_dashboard(request):
    users=User.objects.prefetch_related(
        Prefetch("groups",queryset=Group.objects.all(),to_attr="all_groups")
    ).all()
    
    for user in users:
        if user.all_groups:
            user.group_name=user.all_groups[0].name
        else:
            user.group_name="No Group Name"
            
    counts=User.objects.aggregate(
        admin=Count("id",filter=Q(groups__name="Admin")),
        organiger=Count("id",filter=Q(groups__name="Organiger")),
        participant=Count("id",filter=Q(groups__name="Participant")),
        
    )
            
    return render(request,"admin/dashboard.html",{"users":users,"counts":counts})


def delete_perticipant(request,id):
    if request.method=="POST":
        participant=User.objects.get(id=id)
        participant.delete()
        return redirect("admin_dashboard")