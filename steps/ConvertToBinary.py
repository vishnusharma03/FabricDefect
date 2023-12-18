import os
import json
import base64
from PIL import Image

dataset_path = '../data/train/'
images_folder = 'images/'
labels_folder = 'labels/'

data = []

for filename in os.listdir(f'{dataset_path}{images_folder}'):
    image = Image.open(f'{dataset_path}{images_folder}{filename}')
    image_data = base64.b64encode(image.tobytes())

    label_name = filename.split('.')[0] + '.txt'
    with open(f'{dataset_path}{labels_folder}{label_name}') as f:
        labels = f.read()

    datum = {
        'image': image_data.decode('utf-8'),
        'labels': labels
    }

    data.append(datum)

with open('train.json', 'w') as outfile:
    json.dump(data, outfile)
