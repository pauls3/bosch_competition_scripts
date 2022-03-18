import xml.etree.ElementTree as ET
import os


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


        if img_filename != "":
            for element in root.findall('path'):
                element.text = '/home/stanik/rtis_lab/data/bosch_object_detection_midterm/images/' + img_filename

            tree.write('/home/stanik/rtis_lab/data/bosch_object_detection_midterm/correct_annotations/' + filename)
        else:
            continue