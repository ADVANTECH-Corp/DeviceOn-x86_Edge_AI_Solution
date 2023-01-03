import glob
import xml.etree.ElementTree as ET
import os
from collections import defaultdict
from random import shuffle


people = defaultdict(list)
foam = defaultdict(list)
hand = defaultdict(list)
hat = defaultdict(list)

images = {}

def generate_image_region(basepath):
    dirs = os.listdir(basepath)
    total = 0
    if os.path.isdir(os.path.join(basepath, dirs[0])):
        shuffle(dirs)
        for _dir in dirs:
            total += process_data_for_azure(os.path.join(basepath, _dir), _dir)
    else:
        total += process_data_for_azure(basepath, basepath)

    return images, total

def process_data_for_azure(filepath, dir_name):
    xml_files = glob.glob(os.path.join(filepath, '*.xml'))
    image_files = glob.glob(os.path.join(filepath, '*.jpg'))
    dir_image = {}
    for xml, img in zip(xml_files, image_files):
        tree = ET.parse(xml)
        root = tree.getroot()

        w = root.find("size")[0].text
        h = root.find("size")[1].text

        img_name = img.split('\\')[-1][:-4]

        people_region = []
        foam_region = []
        hand_region = []
        hat_region = []

        temp = {}

        for item in root.findall("object"):
            class_name = item[0].text.replace('-', '')

            x = int(item[4][0].text) / float(w)
            y = int(item[4][1].text) / float(h)
            dw = (int(item[4][2].text) - int(item[4][0].text)) / float(w)
            dh = (int(item[4][3].text) - int(item[4][1].text)) / float(h)

            if class_name == "people":
                people_region.append([x, y, dw, dh])
            if class_name == "foam":
                foam_region.append([x, y, dw, dh])
            if class_name == "hand":
                hand_region.append([x, y, dw, dh])
            if class_name == "hat":
                hat_region.append([x, y, dw, dh])

        temp["people"] = people_region
        temp["foam"] = foam_region
        temp["hand"] = hand_region
        temp["hat"] = hat_region

        dir_image[img_name] = temp

    images[dir_name] = dir_image
    return len(dir_image)

