from django.http import request
from django.shortcuts import render
from .models import comment, resume

# Create your views here.
def home(request):
    resume_obj = resume.objects.all()
    context = {
        'title' : '',
        'resumes': resume_obj,
    }
    return render(request, 'home.html', context)

def about(request):
    resume_obj = resume.objects.all()
    context = {
        'title': '',
        'resumes':resume_obj,

    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'title': 'ติดต่อกับฉัน',
    }
    return render(request, 'contact.html', context)

def blog_page(request, id):
    resume_obj = resume.objects.get(id=id)
    comment_obj = comment.objects.filter(resume=resume_obj).order_by('date_created')

    context = {
        'title' : resume_obj.title,
        'resume' : resume_obj,
        'comments' : comment_obj,
    }
    return render(request, 'blog_page.html', context)