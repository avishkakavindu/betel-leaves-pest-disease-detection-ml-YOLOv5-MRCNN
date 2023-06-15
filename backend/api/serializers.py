from rest_framework import serializers
from .models import Cure


class CureSerializer(serializers.ModelSerializer):
    disease_or_pest_display = serializers.CharField(source='get_disease_or_pest_display', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Cure
        fields = ['id', 'disease_or_pest', 'disease_or_pest_display', 'disease_description',
                  'cure_description', 'type', 'type_display']
