import os

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.response import Response
from rest_framework import status

from .models import Cure
from .serializers import CureSerializer

from .utils import mrcnn_predictor, yolov5_predictor, betel_leaf_predictor

model = mrcnn_predictor.MaskRCNNModel()


class DetectBetelDiseasesAPIView(APIView):
    """ Detects diseases using images """

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            # get image from the request
            file_obj = request.FILES['image']
        except Exception:
            return Response(
                {'msg': 'something is wrong with the uploaded file'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save the uploaded image
        temp_image_file = default_storage.save('disease_detection/temp_image.jpg', ContentFile(file_obj.read()))
        # get saved path
        img_path = os.path.join(settings.MEDIA_ROOT, temp_image_file)

        # run mrcnn and save the image
        pred_to_text = set(model.predict(img_path))

        # Construct the URL for the output image
        image_url = request.build_absolute_uri(settings.MEDIA_URL + temp_image_file)

        cures = {}
        for disease in pred_to_text:
            try:
                cure = Cure.objects.get(disease_or_pest=disease, type=Cure.DISEASE)
                serializer = CureSerializer(cure)
                cures[disease] = serializer.data
            except Cure.DoesNotExist:
                cures[disease] = {
                    'disease': 'Cure not found in database',
                    'disease_description': 'Not found in database'
                }

        context = {
            'image_url': image_url,
            'predictions': pred_to_text,
            'cures': cures
        }

        return Response(context)


class DetectBetelPestAPIView(APIView):
    """ Detect pests using images """

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            # get image from the request
            file_obj = request.FILES['image']
        except Exception:
            return Response(
                {'msg': 'something is wrong with the uploaded file'},
                status=status.HTTP_400_BAD_REQUEST
            )

            # Save the uploaded image
        temp_image_file = default_storage.save('temp_image.jpg', ContentFile(file_obj.read()))
        # get saved path
        img_path = os.path.join(settings.MEDIA_ROOT, temp_image_file)

        try:
            # run mrcnn and save the image
            preds, save_path = yolov5_predictor.run_yolov5_detection(
                img_path=img_path,
                save_to=settings.MEDIA_ROOT,
            )
        except Exception as e:
            return Response(
                {'msg': 'something went wrong while detecting', 'error': e},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        # Delete the original file
        os.remove(img_path)

        # get relative path of detected img
        relative_save_path = os.path.relpath(save_path, settings.MEDIA_ROOT)

        # create url for the image
        image_url = request.build_absolute_uri(settings.MEDIA_URL + relative_save_path)

        cures = {}
        for pest in preds.keys():
            try:
                cure = Cure.objects.get(disease_or_pest=pest, type=Cure.PEST)
                serializer = CureSerializer(cure)
                cures[pest] = serializer.data
            except Cure.DoesNotExist:
                cures[pest] = {
                    'pest': 'Cure not found in database',
                    'disease_description': 'Not found in database'
                }

        context = {
            'predictions': preds,
            'image_url': image_url,
            'cures': cures
        }

        return Response(context)


class BetelLeafTypeClassificationAPIView(APIView):
    """ Classify Betel leaves by image """

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            # get image from the request
            file_obj = request.FILES['image']
        except Exception:
            return Response(
                {'msg': 'something is wrong with the uploaded file'},
                status=status.HTTP_400_BAD_REQUEST
            )

            # Save the uploaded image
        temp_image_file = default_storage.save('temp_image.jpg', ContentFile(file_obj.read()))
        # get saved path
        img_path = os.path.join(settings.MEDIA_ROOT, temp_image_file)

        predictions = betel_leaf_predictor.classify_betel_leaves(img_path)

        context = predictions

        return Response(context)
