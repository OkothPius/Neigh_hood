from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Profile,Neighborhood,Business,EmergencyContacts,Post
from .forms import NeighborhoodForm,UpdateProfileForm,AddBusinessForm,PostForm
from django.contrib.auth.models import User
import datetime

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('signout')
    else:
        if request.user.id == 1:
            if request.method == 'POST':
                form = NeighborhoodForm(request.POST)
                if form.is_valid():
                    neighborhood = Neighborhood(neighborhood_name=request.POST['neighborhood_name'],neighborhood_location=request.POST['neighborhood_location'])
                    neighborhood.save()
                return redirect('home')
            else:
                form = NeighborhoodForm()
            neighborhoods = Neighborhood.objects.all()
            return render(request,'neigh/home.html',{'neighborhoods':neighborhoods,'form':form})
        elif request.user != 1:
            user = Profile.objects.filter(user = request.user).first()
            if user is None:
                user = Profile(user=request.user)
                user.save()
            if user.neighborhood is None:
                title = 'Neighborhood'
                neighborhoods = Neighborhood.objects.all()
                return render(request,'neigh/home.html',{'neighborhoods':neighborhoods})
            else:
                user = Profile.objects.filter(user = request.user).first()
                return redirect(reverse('neighborhood',args=[user.neighborhood.id]))

def signout(request):
    logout(request)
    return redirect('login')


def neighborhood(request,neighborhood_id):
    if request.user.id == 1:
        neighborhood = Neighborhood.objects.get(id = neighborhood_id)
        members = Profile.objects.filter(neighborhood = neighborhood).all()
        emergencies = EmergencyContacts.objects.filter(neighborhood_contact = neighborhood).all()
        return render(request,'neigh/neigh.html',{'neighborhood':neighborhood,'members':members,'emergencies':emergencies})
    else:
        neighborhood = Neighborhood.objects.get(id = neighborhood_id)
        user = Profile.objects.filter(user = request.user).first()
        businesses = Business.objects.filter(business_neighborhood=neighborhood).all()
        emergencies = EmergencyContacts.objects.filter(neighborhood_contact = neighborhood).all()
        user.neighborhood = neighborhood
        user.save()

        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = Post(title=request.POST['title'],post_description=request.POST['post_description'],posted_by=request.user,post_hood=neighborhood,posted_on=datetime.datetime.now())
                post.save()
                return redirect(reverse('neighborhood',args=[neighborhood.id]))
        else:
            form = PostForm()

        posts = Post.objects.filter(post_hood = neighborhood).all()
        return render(request,'neigh/neigh.html',{'posts':posts,'form':form,'user':user,'businesses':businesses,'neighborhood':neighborhood,'emergencies':emergencies})


def profile(request,user_id):
    user = User.objects.get(id = user_id)
    profile = Profile.objects.filter(user = user).first()
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,instance=profile)
        if form.is_valid():
            profile.first_name = request.POST['first_name']
            profile.last_name = request.POST['last_name']
            profile.location = request.POST['location']
            profile.save()
        return redirect(reverse('profile',args=[user.id]))
    else:
        form = UpdateProfileForm(instance=profile)

    businesses = Business.objects.filter(owner = user).all()
    emergencies = EmergencyContacts.objects.filter(neighborhood_contact = profile.neighborhood).all()
    neighborhoods = Neighborhood.objects.all()

    return render(request,'neigh/profile.html',{'neighborhoods':neighborhoods,'businesses':businesses,'profile':profile,'form':form,'emergencies':emergencies})


def add_biz(request):
    user = User.objects.filter(id = request.user.id).first()
    profile = Profile.objects.filter(user = user).first()
    if request.method == 'POST':
        business_form = AddBusinessForm(request.POST)
        if business_form.is_valid():
            business = Business(name = request.POST['name'],owner = user,business_neighborhood = profile.neighborhood,email=request.POST['email'])
            business.save()
        return redirect(reverse('profile',args=[user.id]))
    else:
        business_form = AddBusinessForm()
    return render(request,'neigh/business.html',{'business_form':business_form})


def change_neighborhood(request,neighborhood_id):
    profile = Profile.objects.filter(user = request.user).first()
    neighborhood = Neighborhood.objects.get(id=neighborhood_id)
    profile.neighborhood = neighborhood
    profile.save()
    return redirect(reverse('neighborhood',args=[neighborhood.id]))


def search(request):
    try:
        if 'business' in request.GET and request.GET['business']:
            search_term = request.GET.get('business')
            searched_business = Business.objects.get(name__icontains=search_term)
            return render(request,'neigh/search.html',{'searched_business':searched_business})
    except (ValueError,Business.DoesNotExist):
        message = "Oops! We couldn't find the business you're looking for."
        return render(request,'neigh/search.html',{'message':message})
    return render(request,'neigh/search.html',{'message':message,'searched_business':searched_business})
