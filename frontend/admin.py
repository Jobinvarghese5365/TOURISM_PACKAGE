from django.contrib import admin
from frontend.models import state,destination,Package,Hotel

# Register your models here.
admin.site.register(state)
admin.site.register(destination)
admin.site.register(Package)
admin.site.register(Hotel)