import os

from django.conf import settings

from .yolov5.detect import run as detect

WEIGHT_PATH = os.path.join(settings.BASE_DIR, 'api/utils/trained_models','betel_pest_yolov5/last.pt')
print('\n\n', WEIGHT_PATH)


def run_yolov5_detection(img_path, save_to, augment=True, weights=WEIGHT_PATH):
    """
    Run YOLOv5 detection on an image using the specified parameters.

    Parameters:
        img_path (str): Path to the input image or video file.
        save_to (str): Path to the project directory where results will be saved. Default is None.
        augment (bool): Flag indicating whether to use data augmentation during detection. Default is True.
        weights (str): Path to the YOLOv5 model weights file.

    Returns:
        dict: A dictionary containing the detection results.

    Raises:
        FileNotFoundError: If the specified weights or source file does not exist.
    """

    # Check if source file exists
    if not os.path.isfile(img_path):
        raise FileNotFoundError("Image file not found.")

    # Set the detection parameters
    detect_params = {
        'weights': weights,
        'source': img_path,
        'augment': augment,
        'project': save_to,
        'exist_ok': True,   # save to existing dir?
        'name': 'pest_detection'    # save results to project/name
    }

    # Run YOLOv5 detection
    results, save_path = detect(**detect_params)

    return results, save_path

