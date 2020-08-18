from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import random
from .forms import *
from .models import *
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('admin')
        else:
            messages.error(request, 'Invalid Username and/or Password')

    context = {}
    return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def index(request):
    blogs = Blog.objects.all()

    context = {
        'home': 'active',
        'blogs': blogs
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'about': 'active',
    }
    return render(request, 'about.html', context)

def appointment(request):
    context = {}
    return render(request, 'appointment.html', context)

def blog(request):
    blogs = Blog.objects.all()

    context = {
        'blog': 'active',
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)

def bdetail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blogs = Blog.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.blog = blog
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    context = {
        'blog':blog,
        'blogs':blogs,
        'form':form
    }
    return render(request, 'bdetail.html', context)

def contact(request):
    context = {
        'contact': 'active',
    }
    return render(request, 'contact.html', context)

def faq(request):
    context = {}
    return render(request, 'faq.html', context)

def services(request):
    context = {
        'services': 'active',
    }
    return render(request, 'services.html', context)

def criminal(request):
    context = {
        'services': 'active',
    }
    return render(request, 'criminal.html', context)

def cyber(request):
    context = {
        'services': 'active',
    }
    return render(request, 'cyber.html', context)

def corporate(request):
    context = {
        'services': 'active',
    }
    return render(request, 'corporate.html', context)

def conveyancing(request):
    context = {
        'services': 'active',
    }
    return render(request, 'conveyancing.html', context)

def civil(request):
    context = {
        'services': 'active',
    }
    return render(request, 'civil.html', context)

def probate(request):
    context = {
        'services': 'active',
    }
    return render(request, 'probate.html', context)

def family(request):
    context = {
        'services': 'active',
    }
    return render(request, 'family.html', context)

def testimonial(request):
    context = {
        'testimonial': 'active',
    }
    return render(request, 'testimonial.html', context)