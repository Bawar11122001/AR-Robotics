from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Ttrail/index.html")

def about(request):
    return render(request, "Ttrail/about.html")

def contact(request):
    return render(request, "Ttrail/contact.html")

def blog(request):
    return render(request, "Ttrail/blog.html")

def project(request):
    return render(request, "Ttrail/project.html")

def detail(request):
    return render(request, "Ttrail/detail.html")

def shop(request):
    return render(request, "Ttrail/shop.html")

def team(request):
    return render(request, "Ttrail/team.html")

def testimonial(request):
    return render(request, "Ttrail/testimonial.html")