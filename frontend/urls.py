from django.urls import path
from frontend import views

urlpatterns=[
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Singlepage/<int:id>/',views.Singlepage,name="Singlepage"),
    path('Destination/',views.Destination,name="Destination")
]