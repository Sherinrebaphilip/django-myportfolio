from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects_show=[{"title":"Solving Kidnapped Robot Problem using Find Object 2D","path":"images/robot.png"},
                   {"title":"Quadcopter with Obstacle Avoidance","path":"images/quadcopter.jpg"},
                   {"title":"Accident Detection System using Find Object 2D","path":"images/accident.jpg"}
                   ]
    return render(request, "projects.html",{"projects_show":projects_show})

def experience(request):
    return render(request, "experience.html")

def certificate(request):
    certificates_show=[{"path":"images/udemy_django.jpg"},
                       {"path":"images/flask.jpg"},
                       {"path":"images/machine_learning.jpg"},
                       {"path":"images/nptel.jpg"},]
    return render(request,"certificate.html",{"certificates_show":certificates_show})

def contact(request):
    return render(request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']="attachment";filename="resume.pdf"
            return response
    else:
        return HttpResponse("Resume not found",status=404)
    
def contact_view(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Redirecting to success page")
            return redirect("success")
        else:
            print("Form is not valid",form.errors)
    else:
        form = ContactForm()

    return render(request,"contacts.html",{"form":form})

def success_view(request):
    return render(request, "success.html")