from django.shortcuts import render
from django.http import HttpResponse
from mirna.models import * 

import json

# Create your views here.

def toJSON(objs, status=200):
    j = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(j, status=status, content_type='application/json; charset=utf-8')


def mirna_view(request) :
    
    mirs = mirna.objects.all()

    rst = {}
    rst['name'] = mirs[0].name
    rst['seq'] = mirs[0].seq

    return toJSON(rst, 200)

def mirna_detail_view(request, id) :

    param_seq = id	
    mirs = mirna.objects.get(seq=param_seq)

    rst = {}
    rst['name'] = mirs.name
    rst['seq'] = mirs.seq


    return toJSON(rst, 200)
