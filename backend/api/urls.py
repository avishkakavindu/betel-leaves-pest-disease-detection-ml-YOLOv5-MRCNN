from django.urls import path

from .api_views import DetectBetelDiseasesAPIView, DetectBetelPestAPIView, BetelLeafTypeClassificationAPIView

urlpatterns = [
    path('betel-disease', DetectBetelDiseasesAPIView.as_view(), name='betel-disease'),
    path('betel-pest', DetectBetelPestAPIView.as_view(), name='betel-pest'),
    path('betel-leaf', BetelLeafTypeClassificationAPIView.as_view(), name='betel-leaf')
]