from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
import config
import os

endpoint = config.ENDPOINT
iteration_name = config.ITERATION_NAME
prediction_key = config.PREDICTION_KEY


def get_tags_for_project(angle):
    trainer = CustomVisionTrainingClient(prediction_key, endpoint=endpoint)

    project_id = None
    if angle == 'wet-head-right':
        project_id = config.HEAD_RIGHT
    if angle == 'wet-head-left':
        project_id = config.HEAD_LEFT
    if angle == 'bottling-left':
        project_id = config.BOTTLING_LEFT
    if angle == 'bottling-straight':
        project_id = config.BOTTLING_STRAIGHT
    if angle == 'bottling-right':
        project_id = config.BOTTLING_RIGHT

    results = trainer.get_tags(project_id)

    return results
