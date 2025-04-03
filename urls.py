from django.urls import path
from .views import detect_shoplifting
from .views import index


urlpatterns = [
    path("", index, name="index"),  # Home page
    path("api/detect/", detect_shoplifting, name="detect_shoplifting"),  # API endpoint
]

urlpatterns += [path("", index, name="index")]


