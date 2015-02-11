from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
from student.models import * 

import json

# Create your views here.

def toJSON(objs, status=200):
    j = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(j, status=status, content_type='application/json; charset=utf-8')


def student_view(request) :

    # get student list	
    if request.method == 'GET' :
        sts = Student.objects.all()
        total = Student.objects.all().count()

        rst = {}

        data = []

        for st in sts : 
            st_info = {}
            st_info['id'] = st.id
            st_info['name'] = st.name
            st_info['age'] = st.age
            data.append(st_info)

        rst['data'] = data
        rst['total'] = total

    elif request.method == 'POST' : 
        name = request.POST.get('name')
        age = request.POST.get('age')

        st = Student()
        st.name = name
        st.age = age
        st.save()

        rst = {}
        rst['id'] = st.id
        rst['msg'] = 'OK'    
   
    return toJSON(rst, 200)

def student_detail_view(request, id) :

    if request.method == 'GET' : 
        param_id = id	
        st = Student.objects.get(id=param_id)

        rst = {}
        rst['id'] = st.id
        rst['name'] = st.name
        rst['age'] = st.age

    elif request.method == 'PUT' :
        put = QueryDict(request.body)
        
        param_id = id
        param_name = put.get('name')
        param_age = put.get('age')

        st = Student.objects.get(id=param_id)
        if param_name != "" :
            st.name = param_name
        if param_age != "" : 
            st.age = param_age
     
        st.save()   
      
        rst = {} 
        rst['id'] = st.id
        rst['name'] = st.name
        rst['age'] = st.age

    elif request.method == 'DELETE' :
        delete = QueryDict(request.body)
        
        param_id = id
        st = Student.objects.get(id=param_id)
        st.delete()
     
        rst = {} 
        rst['msg'] = 'OK'

    return toJSON(rst, 200)
