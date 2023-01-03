from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import time
from label_converter import *
import configparser


config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "azure_cv_config.ini"))

## Replace with valid values
ENDPOINT = config["AzureCV"]["ENDPOINT"]
training_key = config["AzureCV"]["training_key"]

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

## Find the object detection domain
obj_detection_domain = next(domain for domain in trainer.get_domains() if domain.type == "ObjectDetection" and
                            domain.name == "General (compact) [S1]")

## Create a new project
print("Creating project...")

## Use custom project name.
project_name = config["AzureCV"]["project_name"]
project = trainer.create_project(project_name, domain_id=obj_detection_domain.id)

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
        
    print(f"Uploaded images : {cnt} / {total_size}")
    cnt += 1
    time.sleep(1)
