### [Azure Custom Vision - Home](https://www.customvision.ai/)
Sign in to start your project

<p align="center">
  <img width="600" src="image\1.png">
</p>

### Create a new project

* Fill out the necessary blanks.(填寫必填欄位內容)

* Use the resource you have created or click `create new` to make a new one.(若沒有`Resource`可以直接點選`create new`新增，若已建立好，則可以選擇既有的)

* In this case, we use object detection to detect items on workstation. Therefore, it should select `Object Detection` on `Project Types`.(本例以物件偵測為主，所以在`Project Types`上選擇`Object Detection`)

* Select the domain that is closest to your application. You can get the information about all the domains from this [website](https://learn.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/select-domain). If you want to export your model, you shall select `General (compact) [S1]` on `Domains`.(若有離線推論的需求，需在`Domains`上選擇`General (compact) [S1]`)
* Export the model, then you can use it to infer offline, and customize your own application.

<p align="center">
  <img width="600" src="image\2.png">
</p>

### Upload training data
> There are two kinds of data to import to custom vision. 1)untagged images; 2)tagged images. 

##### Untagged images
* Click `Add images`, then select the untagged images.(按下`Add images`後，選取欲訓練且未標記的資料)

* After finishing uploading, there will be a red dot sign on `Untagged` button on left side for reminding you.(上傳完成後，左側的`Untagged`會提醒有未標記的圖片)

* It is not necessary to tag all the untagged images to enter training step, but training process can't start without enough training images.(未必要把所有未標記的圖片標記完後才能進行模型的訓練，但是訓練資料量不足時是無法進行訓練的)

<p align="center">
  <img width="600" src="image\3.png">
</p>

##### Tagged images
* The portal doesn’t allow directly uploading your own tagged images, and you have to use [APIs/SDKs](https://learn.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/quickstarts/image-classification?tabs=visual-studio&pivots=programming-language-python) that they support.  

* You can upload up to 64 images in a single batch.

### Label images

* Click `Untagged`, then you can label images.(點選`Untagged`，便可以對裡面的照片進行標記)

<p align="center">
  <img width="600" src="image\4.png">
</p>

<p align="center">
  <img width="600" src="image\5.png">
</p>

* After finishing labeling images, the total amount of each tags will show in down left corner.(標記完後，畫面左下角會顯示各標記類別的數量)

<p align="center">
  <img width="600" src="image\6.png">
</p>
