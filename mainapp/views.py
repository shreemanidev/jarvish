from django.shortcuts import render
def home(Request):
    return render(Request, "index.html")
def contact(Request):
    return render(Request, "contact.html")
def about(Request):
    return render(Request, "about.html")
def projects(Request):
    return render(Request, "projects.html")
def project1(Request):
    return render(Request, "proj1.html")
def blog(Request):
    return render(Request, "blog.html")
def blogDetails(Request):
    return render(Request, "singlepost.html")


    
# Create your views here.
