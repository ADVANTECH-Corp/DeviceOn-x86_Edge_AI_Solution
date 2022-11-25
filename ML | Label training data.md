 ### Sign in [Azure Custom Vision - Home](https://www.customvision.ai/) to start your vision AI project

> Or create your [free Azure account](https://azure.microsoft.com/en-ca/free/) to start

<p align="center">
  <img width="600" src="image\1.png">
</p>

### Create a new project

* Fill out necessary information to proceed the next step.

* Use a project you have created or click `create new` to make a new one.

* In this use case, object detection is used to realize monitoring in a production line. Therefore, it's necessary to select `Object Detection` in `Project Types`.

* Select a suitable domain according to your application. You can get further information about all domains from this [website](https://learn.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/select-domain). PLEASE NOTE if you want to export your model to execute inference at edge (/as an off-line mode), here it's necessary to select `General (compact) [S1]` in `Domains`.

* Then it will be able to export your model to customize your own application and further realize offline inference at edge.

<p align="center">
  <img width="600" src="image\2.png">
</p>

### Upload training data
> There are two categories of data able to be imported to Azure Custom Vision. 1)untagged images; 2)tagged images. 

##### Untagged images
* Click `Add images` and then select untagged images for uploading.

* After finishing uploading, there will be a red dot showing on the `Untagged` button on left side to be a notificaiton.

* It is not necessary to tag all untagged images to proceed the next step for model training, but a training process can't be started without enough training data.

<p align="center">
  <img width="600" src="image\3.png">
</p>

##### Tagged images
* Azure Custom Visoin studio doesn’t support to upload your own tagged images directly, but provides us with [APIs/SDKs](https://learn.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/quickstarts/image-classification?tabs=visual-studio&pivots=programming-language-python) to fulfill this end.

* You can upload up to 64 images in a single batch in an app developed with the above-mentioned APIs/SDKs.

### Label images

* Click `Untagged` and then you can start to label images through its friendly UI/UX design. ( Moreover you also can enjoy auto-labeling if you already have at least one trained model in the project.)

<p align="center">
  <img width="600" src="image\4.png">
</p>

<p align="center">
  <img width="600" src="image\5.png">
</p>

* After finishing labeling images, the amount of each tag will show in down left corner.

<p align="center">
  <img width="600" src="image\6.png">
</p>
