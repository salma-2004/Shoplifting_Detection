from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
import os
from .models import predict

@api_view(['POST'])
def detect_shoplifting(request):
    if 'video' not in request.FILES:
        return JsonResponse({"error": "No video file provided"}, status=400)

    video_file = request.FILES['video']
    video_path = f"temp/{video_file.name}"

    os.makedirs("temp", exist_ok=True)
    with open(video_path, "wb") as f:
        for chunk in video_file.chunks():
            f.write(chunk)

    result = predict(video_path)
    os.remove(video_path)

    return JsonResponse(result)

def index(request):
    return render(request, "detection/index.html")


