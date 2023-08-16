from django.urls import path, include
from .views import *
urlpatterns = [
    path('',index,name="landing"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('blog/',blog,name="blog"),
    path('project/',project,name="project"),
    path('detail/',detail,name="detail"),
    path('shop/',shop,name="shop"),
    path('team/',team,name="team"),
    path('testimonial/',testimonial,name="testimonial"),
]