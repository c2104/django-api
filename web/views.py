from django.shortcuts import render
from api.models import AiAnalysisLog
from datetime import datetime

import requests
import json

def index(request):
    return render(request, 'web/index.html')

def save(request):
    request_timestamp = int(datetime.now().timestamp())

    r = request_api(request.POST['image_path'])
    response_timestamp = get_response_timestamp(r.headers['Date'])

    response = r.json()
    save_parameter = {
        'image_path' : request.POST['image_path'],
        'success' : response['success'],
        'message' : response['message'],
        'class' : response['estimated_data'].get('class', None),
        'confidence' : response['estimated_data'].get('confidence', None),
        'request_timestamp' : request_timestamp,
        'response_timestamp': response_timestamp
    }

    save_log(save_parameter)

    return render(request, 'web/result.html', {'message' : '保存しました'})

def request_api(image_path):
    return requests.post(
        'http://localhost:9003/api/v1/',
        headers = {'Content-Type': 'application/json'},
        data = json.dumps({'image_path' : image_path}),
        timeout = 1
    )

def save_log(parameter):
    ai_analysis_log = AiAnalysisLog(
        image_path = parameter['image_path'],
        success = parameter['success'],
        message = parameter['message'],
        classes = parameter['class'],
        confidence = parameter['confidence'],
        request_timestamp = parameter['request_timestamp'],
        response_timestamp = parameter['response_timestamp'],
    )

    ai_analysis_log.save()

def get_response_timestamp(response_header_date):
    response_datetime = datetime.strptime(response_header_date, '%a, %d %b %Y %H:%M:%S %Z')
    return int(response_datetime.timestamp())

