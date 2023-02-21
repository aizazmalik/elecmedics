"""elecmedics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainapp.filters import PrescriptionFilterSet

from mainapp.models import Patient, Prescription

admin.site.site_header = "Al Aziz Hospital"
admin.site.index_title = "Welcome to Al Aziz Hospital"
admin.site.site_title = "Al Aziz Hospital"

class PatientAdmin(admin.ModelAdmin):
    search_fields = ['patient_name', 'cnic', 'father_name', 'mobile_number']
    list_filter = ['patient_name', 'cnic', 'father_name', 'mobile_number']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        selected_field = request.GET.get('field')
        if selected_field:
            qs = qs.filter(**{selected_field: request.GET.get('q')})
        return qs

class PrescriptionAdmin(admin.ModelAdmin):
    search_fields = ["token_number","patient_id__id"]
    list_filter = ["token_number","patient_id__id"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        selected_field = request.GET.get('field')
        if selected_field:
            qs = qs.filter(**{selected_field: request.GET.get('q')})
        return qs


admin.site.register(Patient,PatientAdmin)
admin.site.register(Prescription, PrescriptionAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('login/', include('login.urls')),
    path('app/', include('mainapp.urls')),
]
