from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import config
import os

endpoint = config.ENDPOINT
iteration_name = config.ITERATION_NAME
prediction_key = config.PREDICTION_KEY


def find_seal(image_path, angle):
    predictor = CustomVisionPredictionClient(prediction_key, endpoint=endpoint)

    project_id = None
    if angle == 'head-right':
        project_id = config.HEAD_RIGHT
    if angle == 'head-left':
        project_id = config.HEAD_LEFT
    if angle == 'bottling-left':
        project_id = config.BOTTLING_LEFT
    if angle == 'bottling-straight':
        project_id = config.BOTTLING_STRAIGHT
    if angle == 'bottling-right':
        project_id = config.BOTTLING_RIGHT

    # Open the image and get back the prediction results.
    with open(image_path, mode="rb") as image_contents:
        results = predictor.classify_image(
            project_id, iteration_name, image_contents.read())

    image_predictions = {}

    for prediction in results.predictions:
        image_predictions[prediction.tag_name] = prediction.probability
        print ("\t" + prediction.tag_name +
               ": {0:.2f}%".format(prediction.probability * 100))

    return image_predictions


def id_seal(image_path, angle):
    return find_seal(image_path, angle)
