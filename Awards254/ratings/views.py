from django.shortcuts import render
from .models import *
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DisplayProjectForm


# Create your views here.

def index(request):
    
 
    return render(request, 'all-awards/index.html', )

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    projects = Project.objects.filter(user_id=current_user.id)
    
    return render(request,"profile.html",{'profile':profile,'projects':projects})
@login_required(login_url='/accounts/login/')
def uploadprofile(request):
    if request.method == 'POST':
        form=DisplayProjectForm(request.POST,request.FILES)
        if form.is_valid():
            image =form.save(commit=False)
            image.save()
            return redirect('/')
        else:
            form=DisplayProjectForm()
        return render(request,"show_pic.html",{'form':form})