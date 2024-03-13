from django.urls import path
from frontend import views

urlpatterns=[
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Singlepage/',views.Singlepage,name="Singlepage"),
]