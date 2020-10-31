from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Shivam Shekhar',
        'title': 'Blog Post 1',
        'content': 'This is the first blog post. So excited to be a part',
        'date_posted': 'October 31, 2020'
    },
    {
        'author': 'Superman',
        'title': 'Ispaiderman',
        'content': 'Spiderman is a piece of shit superhero. I am the only OP superhero, and that is a fact',
        'date_posted': 'October 5, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')