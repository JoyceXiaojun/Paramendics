from django.shortcuts import render
from django.http import HttpResponse
from paramedic.models import Hospital
from paramedic.models import Patient
from paramedic.models import MedicalInstr
from datetime import datetime
import json

# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")
'''
def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
'''

def paramedic_home(request):
    return render(request, 'paramedic_home.html', {'title': 'menu'})

def paramedic_patientinfo(request):
    return render(request, 'patient_info.html', {'title': 'patient'})

def paramedic_info_detail(request):
    return render(request, 'patient_info_detail.html',{'title': 'patient'})

def paramedic_hospital(request):
    return render(request, 'hospital.html', {'title': 'hospital'})

def paramedic_map(request):
    return render(request, 'map.html', {'title': 'map'})

def paramedic_instruction(request):
    return render(request, 'medical.html', {'title': 'instruction'})

def paramedic_list(request):
    return render(request, 'druglist.html', {'title': 'instruction'})

def report(request) :
    return render(request, 'report.html', {'title': 'report'})

def patient_detail(request, id):
    data = {
        'name':'Paul Smith',
        'pid':'123456789',
        'contacts':'Tony: 123-123-1234',
        'contacts2':'Brian: 456-123-4567',
        'medical1':'Heart Attack: 10-11-2015',
        'medical2':'Medicine: Aspirin'
    }
    return render(request, 'patient_info_detail.html', {'title': 'patient', 'data': data})


def medical_drug(request):
    return render(request, 'druglist.html', {'title':'drug','type':1})

def medical_refer(request):
    return render(request, 'druglist.html', {'title':'refer','type':2})

def medical_prot(request):
    return render(request, 'druglist.html', {'title':'protocal','type':3})

def medical_tool(request):
    return render(request, 'druglist.html', {'title':'tool','type':4})

def search_patient(request):
    data = [{
        'name':'Paul Smith',
        'pid':'123456789',
        'contacts':'Tony: 123-123-1234',
        'contacts2':'Brian: 456-123-4567',
        'medical1':'Heart Attack: 10-11-2015',
        'medical2':'Medicine: Aspirin'
    }]
    return HttpResponse(json.dumps(data, ensure_ascii=False))

def search_medical(request):
    name = request.GET.get('name')
    type = int(request.GET.get('type'))
    data = []
    if type == 1:
        data.append({
            'id':1,
            'name':'drug1',
            'type':1,
            'intro':'This is a drug'
        })
    elif type == 2:
        data.append({
            'id':1,
            'name':'reference1',
            'type':2,
            'intro':'This is a reference'
        })
    elif type == 3:
        data.append({
            'id':1,
            'name':'protocal1',
            'type':3,
            'intro':'This is a protocal'
        })
    else:
        data.append({
            'id':1,
            'name':'tool1',
            'type':4,
            'intro':'This is a tool'
        })

    return HttpResponse(json.dumps(data, ensure_ascii=False))

def medical_detail(request, id):
    return render(request, 'drug_detail.html', {'title':'Instructiion'})

def search_hospital(request):
    data = [{
        'id':1,
        'name':'EI Camino Hospital',
        'x-ray': True,
        'lat':37.368115,
        'lon':-122.079750
    }, {
        'id':2,
        'name':'Palo Alto Hospital',
        'x-ray': True,
        'lat':37.461332,
        'lon':-122.158353
    }]
    return HttpResponse(json.dumps(data, ensure_ascii=False))
