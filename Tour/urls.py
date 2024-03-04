from django.urls import path
from Tour import views

urlpatterns = [
    path('Tour_page/', views.Tour_page, name="Tour_page"),
    path('Tour_packages/', views.Tour_packages, name="Tour_packages"),
    path('Packages_save/', views.Packages_save, name="Packages_save"),
]