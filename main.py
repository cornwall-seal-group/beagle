from flask import Flask, url_for, send_from_directory, request, jsonify
import logging
import os
import time
import config
from classifier.id import id_seal
from werkzeug.utils import secure_filename
import shutil

app = Flask(__name__)
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

IMAGES_FOLDER = config.IMAGES_FOLDER
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/guess-image', methods=['POST'])
def guess_seal_in_image():
    # check file is an image before uploading

    # send image for object detection and get predictions
    # create an image for each prediction and save in folder

    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            return "Where is the image?"

        file = request.files['file']

        if request.angle == '':
            return "The angle is empty, please supply an angle"

        angle = request.angle
        if file and allowed_file(file.filename):

            epoch_time = int(time.time())
            folder_path = IMAGES_FOLDER + str(epoch_time) + '/'

            directory = os.path.dirname(folder_path)
            os.makedirs(directory)

            filename = secure_filename(file.filename)
            image_path = os.path.join(folder_path, filename)
            file.save(image_path)
            print 'Saving image to ' + image_path

            ids = id_seal(image_path, angle)

    return ids


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
