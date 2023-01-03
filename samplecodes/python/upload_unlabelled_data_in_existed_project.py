import os
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
import configparser
import glob
import time

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "azure_cv_config.ini"))

## Replace with valid values
ENDPOINT = config["AzureCV"]["ENDPOINT"]
training_key = config["AzureCV"]["training_key"]

project_id = config["AzureCV"]["project_id"]
base_image_location = config["AzureCV"]["image_dir"]
print(f"training_key: {training_key}")

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

print("trainer start")
project = trainer.get_project(project_id=project_id)

base_image_location = config["AzureCV"]["image_dir"]
image_path = glob.glob(os.path.join(base_image_location, "*.jpg"))
total_size = len(image_path)
cnt = 1
for img_path in image_path:
    untagged_images = []
    with open(img_path, mode="rb") as image_contents:
        name = img_path.split("\\")[-1].replace(".jpg", "")
        untagged_images.append(ImageFileCreateEntry(name=name, contents=image_contents.read()))

    upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=untagged_images))
    if not upload_result.is_batch_successful:
        print("Image batch upload failed.")
        for result_image in upload_result.images:
            print("Image status: ", result_image.status)
        exit(-1)
    
    print(f"Uploaded images: {cnt} / {total_size}")
    cnt += 1
    time.sleep(1)
