from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#import request
from datetime import datetime
# Create your views here.
@api_view(["GET"])
def get_status(request):
    current_date=datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day_name = current_date.strftime("%A")
    response_data = {
        "slack_name":request.query_params.get('slack_name'),
        "current_day":current_day_name,
        "utc_time":formatted_datetime,
        "track":request.query_params.get("track"),
        "github_file_url":"https://github.com/Couzy21/HNG/blob/couzy/api/views.py",
        "github_repo_url":"https://github.com/Couzy21/HNG",
        "status_code":status.HTTP_200_OK,
          }
    return Response(response_data)