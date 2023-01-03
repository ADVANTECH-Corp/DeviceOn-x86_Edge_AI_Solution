# Collect data for model retraining

## Batch-upload new training data
* It would be more efficient for you to use `Azure Custom Vision SDKs` to upload training data.
* Firstly, install [`azure-cognitiveservices-vision-customvision`](https://pypi.org/project/azure-cognitiveservices-vision-customvision/) and [`msrest`](https://pypi.org/project/msrest/) by using [pip3](https://pypi.org/project/pip/).
```
$ pip3 install azure-cognitiveservices-vision-customvision
$ pip3 install msrest
```
> You can find other Cognitive Services modules [here](https://learn.microsoft.com/en-us/python/api/overview/azure/cognitive-services?view=azure-python).

* Secondly, if you label your images in `PASCAL VOC` format and save them as .xml files, you have to convert the original format to the format of Azure Custom Vision. Here lists the sample codes to convert 4 labels (people, foam, hand, hat). 

```
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

        temp["people"] = People_region
        temp["foam"] = Foam_region
        temp["hand"] = hand_1_region
        temp["hat"] = hat_region
        
        dir_image[img_name] = temp

    images[dir_name] = dir_image
    return len(dir_image)
```
 
* Finally, prepare your data, and there are four cases for uploading your data. These cases arw shown below.

|                  | new project   | existed project |
| ---------------- |:-------------:|:---------------:|
| labeled images   | case 1        | case 2          |
| unlabeled images | case 3        | case 4          |

> NOTICE: An existed project without any labeled images or any tags is not allowed in this practice. 

> NOTICE: `tags` in [`azure_cv_config.ini`](/sample%20codes/python/azure_cv_config.ini) must be consistant with tags in Azure Custom Vision.

<p align="center">
  <img width="800" src="image\49-1.png">
</p>

case 1. [Uploading labelled data to a new project](https://github.com/ADVANTECH-Corp/DeviceOn-x86_Edge_AI_Solution_Internal/blob/main/sample%20codes/python/upload_labelled_data_in_new_project.py)

* In this case, you don't have to add a new project manually. You just fill out all items except `prediction_key` and `project_id` in the [`azure_cv_config.ini`](/sample%20codes/python/azure_cv_config.ini), and your project will be built.

* `training_key` and `ENDPOINT` can be found in your custom vision in Azure Protal.

<p align="center">
  <img width="800" src="image\50.png">
</p>

case 2. [Uploading labelled data to an existed project](https://github.com/ADVANTECH-Corp/DeviceOn-x86_Edge_AI_Solution_Internal/blob/main/sample%20codes/python/upload_labelled_data_in_existed_project.py)

* In this case, fill The [`azure_cv_config.ini`](/sample%20codes/python/azure_cv_config.ini), out and then execute the python codes.

* Required information can be found in the `Settings`, where is located by red arrow, of your Azure Custom Vision project.

<p align="center">
  <img width="800" src="image\49.png">
</p>

case 3. [Uploading unlabelled data to a new project](https://github.com/ADVANTECH-Corp/DeviceOn-x86_Edge_AI_Solution_Internal/blob/main/sample%20codes/python/upload_unlabelled_data_in_new_project.py)

* Follow case 1 to fill out the [`azure_cv_config.ini`](/sample%20codes/python/azure_cv_config.ini) correctly.

<p align="center">
  <img width="400" src="image\50-1.png">
</p>

case 4. [Uploading unlabelled data to an existed project](https://github.com/ADVANTECH-Corp/DeviceOn-x86_Edge_AI_Solution_Internal/blob/main/sample%20codes/python/upload_unlabelled_data_in_existed_project.py)

* Follow case 2 to fill out the [`azure_cv_config.ini`](/sample%20codes/python/azure_cv_config.ini) correctly, except `tags`.

<p align="center">
  <img width="400" src="image\50-2.png">
</p>

Take `Uploading labelled data to a new project` for example, here is the command to execute [upload_labelled_data_in_new_project.py](/sample%20codes/python/upload_labelled_data_in_new_project.py).

```
$ python3 upload_labelled_data_in_new_project.py
```
