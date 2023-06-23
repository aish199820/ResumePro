from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('skill/',views.skills_view,name="skills"),
    path('contact/',views.contact_view,name="contact"),
    path('education/',views.eduction_view,name="education"),
    path('course/',views.courses_view,name="courses"),
    path('experience/',views.experience_view,name="experiences"),
    path('project/',views.project_view,name="project"),
    path('health/',views.health_view,name="health"),
    path('shop/',views.shop_view,name='shop'),
]