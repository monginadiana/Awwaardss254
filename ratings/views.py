

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm, DisplayProjectForm, UpdateProfileForm

from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from .models import Profile,Project,Rating
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework.views import APIView
from .permissions import  IsAdminOrReadOnly
from ratings import serializer


# Create your views here.

def index(request):
   
    workks = Project.objects.all().order_by('-id')
    return render(request, 'all-awards/index.html',{'workks':workks})
#Create profile for updating projects
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
#Create user Proffile
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
#Update USer Profile
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
    return render(request, 'all-awards/update_profile.html', ctx)

def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    rating = Rating.objects.filter(project = project)
    # get project rating
    return render(request, "all-awards/project_details.html", {"project": project, "rating": rating})

# rate_project
@login_required(login_url='/accounts/login/')
def rate(request,id):
    if request.method == 'POST':
        project = Project.objects.get(id = id)
        current_user = request.user
        design_rate = request.POST['design']
        content_rate = request.POST['content']
        usability_rate = request.POST['usability']

        Rating.objects.create(
            project=project,
            user=current_user,
            design_rate=design_rate,
            usability_rate=usability_rate,
            content_rate=content_rate,
            avg_rate=round((float(design_rate)+float(usability_rate)+float(content_rate))/3,2),)

        return render(request,"all-awards/project_details.html",{"project":project})
    else:
        project = Project.objects.get(id = id) 
        return render(request,"all-awards/project_details.html",{"project":project})
    
@login_required(login_url='/accounts/login/')
def search_project(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        projects = Project.search_project_name(search_term)
        message = f'{search_term}'

        return render(request, 'all-awards/search.html', {'found': message, 'projects': projects})
    else:
        message = 'Not found'
        return render(request, 'all-awards/search.html', {'danger': message})
    
class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects,many=True)
        return Response(serializer.data)

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles,many=True)
        return Response(serializer.data)