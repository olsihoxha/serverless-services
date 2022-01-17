import base64
import json
from io import BytesIO

import cv2
from imageio import imread


def detect_faces(event, context):
    try:
        image_base64 = event['image']
        face_cascade = cv2.CascadeClassifier('../helper_files/haarcascade_frontalface_default.xml')
        b64_string = image_base64.decode()
        img = imread(BytesIO(base64.b64decode(b64_string)))
        cv2_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            cv2_img,
            1.05,
            4
        )

        faces_data = []

        for (x, y, w, h) in faces:
            faces_data.append({'x': x, 'y': y, 'width': w, 'height': h})
        return {
            'statusCode': 200,
            'body': json.dumps({'all_face_data': faces_data})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'errorMessage': f'Something went wrong. Error: {str(e)}'})
        }
