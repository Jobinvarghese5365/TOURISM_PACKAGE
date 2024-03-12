from django.urls import path
from Tour import views

urlpatterns = [
    path('Tour_page/', views.Tour_page, name="Tour_page"),
    path('Tour_packages/', views.Tour_packages, name="Tour_packages"),
    path('Packages_save/', views.Packages_save, name="Packages_save"),
    path('Display_Packages/', views.Display_Packages, name="Display_Packages"),
    path('update_category<int:c_id>/', views.update_category, name="update_category"),
    path('Edit_Packages<int:c_id>/', views.Edit_Packages, name="Edit_Packages"),
    path('Delete_Package<int:c_id>/', views.Delete_Package, name="Delete_Package"),
]