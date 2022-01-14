import base64
import json
from io import BytesIO

import speech_recognition as sr


def generate_text(event, context):
    reader = sr.Recognizer()

    file_encoded = event['audio']
    file_bytes = base64.b64decode(file_encoded)
    file = BytesIO(file_bytes)
    try:
        with sr.AudioFile(file) as source:
            audio_text = reader.listen(source)

            text = reader.recognize_google(audio_text)
            print('Converting audio transcript to text...')
            return {
                'statusCode': 200,
                'body': json.dumps({'text': text})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'errorMessage': f'Something went wrong. Error: {str(e)}'})
        }
