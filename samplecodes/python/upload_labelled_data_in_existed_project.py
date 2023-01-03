from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import time
from label_converter import *
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "azure_cv_config.ini"))

ENDPOINT = config["AzureCV"]["ENDPOINT"]
training_key = config["AzureCV"]["training_key"]
project_id = config["AzureCV"]["project_id"]

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
project = trainer.get_project(project_id=project_id)
tags = trainer.get_tags(project_id=project_id)

tag_ids = {}
for tag in tags:
    tag_ids[tag.name] = tag.id


## Upload labeled images
base_image_location = config["AzureCV"]["image_dir"]
labeled_images, total_size = generate_image_region(base_image_location)

## Go through the data table above and create the images
image_size = len(glob.glob(os.path.join(base_image_location, "*.jpg")))
print("Adding images...")

cnt = 1
for dir in labeled_images.keys():
    for image in labeled_images[dir].keys():
        tagged_images_with_regions = []
        regions = []
        for tag in labeled_images[dir][image].keys():
            for bndbox in labeled_images[dir][image][tag]:
                if bndbox == []:
                    continue
                x, y, w, h = bndbox
                regions.append(Region(tag_id=tag_ids[tag], left=x, top=y, width=w, height=h))

        with open(os.path.join(base_image_location, dir, image + ".jpg"), mode="rb") as image_contents:
            tagged_images_with_regions.append(ImageFileCreateEntry(name=image, contents=image_contents.read(), regions=regions))

        upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=tagged_images_with_regions))

        if not upload_result.is_batch_successful:
            print("Image batch upload failed.")
            for result_image in upload_result.images:
                print(f"Image status: {result_image.status}")
            exit(-1)

        print(f"Uploaded images : {cnt} / {total_size}")
        cnt += 1
        time.sleep(1)

