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

def homepage(request):
    return render(request, 'home.html')

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
        'medical2':'Allergy Medicine: Aspirin'
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
            'id':0,
            'name':'Aspirin',
            'type':1,
            'intro':'This is a drug'
        })
        data.append({
            'id':1,
            'name':'ACE inhibitors',
            'type':1,
            'intro':'This is a drug'
        })
        data.append({
            'id':2,
            'name':'Beta-blockers',
            'type':1,
            'intro':'This is a drug'
        })
        data.append({
            'id':3,
            'name':'Cholesterol-lowering drugs',
            'type':1,
            'intro':'This is a drug'
        })
    elif type == 2:
        for i in range(0, 20):
            data.append({
                'id':i,
                'name':'reference' + str(i),
                'type':2,
                'intro':'This is a reference'
            })
    elif type == 3:
        for i in range(0, 20):
            data.append({
                'id':i,
                'name':'protocal' + str(i),
                'type':3,
                'intro':'This is a protocal'
            })
    else:
        for i in range(0, 20):
            data.append({
                'id':i,
                'name':'tool' + str(i),
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

def patient_location(request):
    patients = [{
        'name':'Paul Smith',
        'pid':'123456789',
        'lat':37.427588,
        'lon':-122.171504
    }]
    return HttpResponse(json.dumps(patients, ensure_ascii=False))

def hospital_location(request):
    hid = int(request.GET.get('id'))
    data = None
    hospitals = [{
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

    if hid == 1:
        data = hospitals[0]
    else:
        data = hospitals[1]

    return HttpResponse(json.dumps(data, ensure_ascii=False))