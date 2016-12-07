"""EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from paramedic import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.home),
    url(r'^paramedic/home', views.paramedic_home),
    url(r'^paramedic/patient_info', views.paramedic_patientinfo),
    url(r'^paramedic/instruction', views.paramedic_instruction),
    url(r'^paramedic/report', views.report),
    url(r'^paramedic/map', views.paramedic_map),
    url(r'^paramedic/hospital_info', views.paramedic_hospital),
    url(r'^paramedic/patient/(?P<id>\d+)/$', views.patient_detail),
    url(r'^paramedic/patient/search', views.search_patient),

    url(r'^paramedic/medical/drug', views.medical_drug),
    url(r'^paramedic/medical/refer', views.medical_refer),
    url(r'^paramedic/medical/protocal', views.medical_prot),
    url(r'^paramedic/medical/tool', views.medical_tool),

    url(r'^paramedic/medical/search', views.search_medical),
    url(r'^paramedic/medical/(?P<id>\d+)/$', views.medical_detail),

    url(r'^paramedic/hospital/search', views.search_hospital),
]

