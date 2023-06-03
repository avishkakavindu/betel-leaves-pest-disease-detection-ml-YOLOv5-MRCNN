from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from datetime import datetime
import skimage.io
from rest_framework import status
import os
import sys



from .models import Cure

model = ''


class DetectBetelDiseasesAPIView(APIView):
    """ Detects diseases using images """

    def post(self, request, *args, **kwargs):
        context = {
            'msg': 'hello world'
        }
        return Response(context)


class DetectBetelPestAPIView(APIView):
    pass
