from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about,name="about"),
    path("project/",views.projects, name="projects"),
    path("experience/",views.experience, name="experience"),
    path("certificate/",views.certificate, name="certificate"),
    path("contact/",views.contact_view, name="contact"),
    path("resume/", views.resume, name="resume"),
    path("success/",views.success_view, name="success"),
]
