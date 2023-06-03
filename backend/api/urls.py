from django.urls import path

from .api_views import DetectBetelDiseasesAPIView, DetectBetelPestAPIView

urlpatterns = [
    path('betel-disease', DetectBetelDiseasesAPIView.as_view(), name='coconut-disease'),
    path('betel-pest', DetectBetelPestAPIView.as_view(), name='cinnamon-disease')
]