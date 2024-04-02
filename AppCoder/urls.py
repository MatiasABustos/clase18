from django.urls import path
from . import views

urlpatterns = [
    path ("", views.inicio , name = "home"),
    path ("ver_cursos/", views.ver_cursos , name = "cursos"),
    path ('alta_curso/<nombre>/', views.alta_curso),
    path ('alumnos/', views.alumnos , name = "alumnos"),
    path ('profesores/', views.profesores , name = "profesores")
    
]