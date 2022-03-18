import os
import numpy as np
from sklearn.model_selection import train_test_split
import shutil
import xml.etree.ElementTree as ET


directory = '/home/stanik/rtis_lab/data/bosch_object_detection_midterm/images'

images_arr = []

for filename in os.listdir(directory):
    #f = os.path.join(directory, filename)
    images_arr.append(filename)

y = np.zeros(len(images_arr))

x_train, x_test, y_train, y_test = train_test_split(images_arr, y, test_size=0.2, random_state=117)


for file0 in x_train:
    print(os.path.join('/home/stanik/rtis_lab/data/bosch_object_detection_midterm/images/train', file0))
    shutil.copy(os.path.join(directory, file0), os.path.join('/home/stanik/rtis_lab/data/bosch_object_detection_midterm/images/train', file0))

for file0 in x_test:
    shutil.copy(os.path.join(directory, file0), os.path.join('/home/stanik/rtis_lab/data/bosch_object_detection_midterm/images/val', file0))


directory = '/home/stanik/rtis_lab/data/bosch_object_detection_midterm/annotations'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        tree = ET.parse(f)
        root = tree.getroot()

        img_filename = ""
        #ET.SubElement(root[0], 'filename')
        for element in root.findall('filename'):
           img_filename = element.text
           print(img_filename)

        if img_filename in x_train:
            img_root = 'train'
        else:
            img_root = 'val'


        if img_filename != "":
            for element in root.findall('path'):
                element.text = os.path.join('/home/stanik/rtis_lab/data/bosch_object_detection_midterm/images/', img_root, img_filename)

            tree.write('/home/stanik/rtis_lab/data/bosch_object_detection_midterm/correct_annotations/' + filename)
        else:
            continue