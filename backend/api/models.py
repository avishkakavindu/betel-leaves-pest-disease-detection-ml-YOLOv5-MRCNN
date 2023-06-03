from django.db import models

# Create your models here.
from django.db import models


class Cure(models.Model):
    # disease
    BACTERIA_LEAF_BLIGHT = 'bacterial_leaf_blight'
    LEAF_SPOT = 'leaf_spot'
    STEM_DISEASE = 'stem_disease'

    # pest
    MEALY_BUG = 'mealybug'
    WHITE_FLY = 'whitefly'

    PEST = 'pest'
    DISEASE = 'disease'

    DISEASE_CHOICES = [
        (BACTERIA_LEAF_BLIGHT, 'Bacteria Leaf Blight'),
        (LEAF_SPOT, 'Leaf Spot'),
        (STEM_DISEASE, 'Stem Disease'),

        (MEALY_BUG, 'Mealy Bug'),
        (WHITE_FLY, 'White Fly')
    ]

    TYPE = [
        (PEST, 'Pest'),
        (DISEASE, 'Disease')
    ]

    disease_or_pest = models.CharField(max_length=255, choices=DISEASE_CHOICES)
    cure_description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE, default=DISEASE)

    def __str__(self):
        return f'{self.get_type_display()} - {self.get_disease_or_pest_display()}'