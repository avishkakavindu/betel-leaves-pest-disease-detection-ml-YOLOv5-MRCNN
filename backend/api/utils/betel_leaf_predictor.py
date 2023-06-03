import os
import cv2
import numpy as np
from django.conf import settings
from tensorflow.keras.models import load_model


CLASSES = ['Maneru', 'Naagawalli']
MODEL_PATH = os.path.join(settings.BASE_DIR, 'api/utils/trained_models', 'betel_leaves_identification/leaf_identification_model.h5')


def get_processed_input_img(image_path, size=224):
    """
    Preprocess the image
    :param image_path: Path for the image
    :param size: size of the image
    :return: normalized image array
    """
    test_img = cv2.imread(image_path)
    test_img = cv2.resize(test_img, dsize=(size, size), interpolation=cv2.INTER_AREA)

    test_img = test_img.reshape((1, size, size, 3)).astype(np.float32)

    return test_img/225


def classify_betel_leaves(img_path, model_path=MODEL_PATH, size=224):
    # preprocess image
    processed_img = get_processed_input_img(image_path=img_path, size=size)

    # load trained model
    loaded_model = load_model(model_path)

    pred = loaded_model.predict(processed_img)

    # inversely sorted array with indexes
    best_idx = (-pred).argsort()[0]

    # Convert predictions to formatted dictionaries
    predictions = [
        {
            'prediction': CLASSES[i],
            'probability': round(float(pred[0][i]) * 100, 2)
        }
        for i in best_idx
    ]

    return predictions
