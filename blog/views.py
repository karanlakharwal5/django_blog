from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'Karan Lakarwal',
        'title':'Blog Post 1',
        'content':'First post contnet',
        'date_posted':'August 30,2020'
    },
    {
        'author':'Tanu Sidana',
        'title':'Blog Post 2',
        'content':'Second post contnet',
        'date_posted':'September 30,2020'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html')






