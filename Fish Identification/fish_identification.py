import json , time
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import requests
import shutil
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img , img_to_array
from keras.models import load_model
import efficientnet.tfkeras as efn
import cv2

fish_identification_model = load_model('fish_identification.h5')

class_labels = ['Alagoduwo','paraw','Kelawalla','Balaya']

def prediction(url):
    test_image = cv2.imread(url) 
    test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
    test_image = cv2.resize(test_image, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    predict_image = np.expand_dims(test_image, axis = 0)
    probability_list = fish_identification_model.predict(predict_image)
    return class_labels[np.argmax(probability_list)]

app = Flask(__name__)
@app.route('/fish_indentification', methods=['POST'])
def fish_indentification():
    try:
        request_data = request.get_json()

        print(request_data['url'])

        image_url = str(request_data['url'])
        filename = image_url.split("/")[-1]
        filename = filename.split("?alt=media&token")[0]
        filename = filename.split("-")[0]
        filename = filename.split("%")[1]+'.jpg'

        r = requests.get(image_url, stream = True)

        if r.status_code == 200:
            r.raw.decode_content = True
            
            with open('downloads/'+filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image Downloaded: ','downloads/'+filename)

            value =prediction('downloads/'+filename)

            json_dump = json.dumps({"value":value,"success":"true"})

            return json_dump
        else:
            json_dump = json.dumps({"value":"","success":"false"})

            return json_dump
    except:
        print("An exception occurred")
        json_price = json.dumps({"success":"false"})

        return json_price

if __name__ == '__main__':
	app.run(host="127.0.0.1", port=7777)