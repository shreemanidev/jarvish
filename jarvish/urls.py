from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [                                
    path('admin/', admin.site.urls),
    path('',views.home),
    path('contact/',views.contact),
    path('about/',views.about),
    path('projects/',views.projects),
    path('project1/',views.project1),
    path('blog/',views.blog),
    path('blog-details/',views.blogDetails),
  
]
    
