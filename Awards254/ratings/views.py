

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm, DisplayProjectForm, UpdateProfileForm


# Create your views here.

def index(request):
   
    workks = Project.objects.all().order_by('-id')
    return render(request, 'all-awards/index.html',{'workks':workks})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    projects = Project.objects.filter(user_id=current_user.id)
    
    return render(request,"profile.html",{'profile':profile,'projects':projects})
@login_required(login_url='/accounts/login/')
def upload_project(request):
    if request.method == 'POST':
        form=DisplayProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project =form.save(commit=False)
            project.save()
            return redirect('/')
    else:
        form=DisplayProjectForm()
    return render(request,"all-awards/upload_project.html",{'form':form})

def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = CreateProfileForm()
    return render(request, 'all-awards/create_profile.html', {"form": form, "title": title})

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():      
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    ctx = {"form":form}
    return render(request, 'all-awards/create_profile.html', ctx)