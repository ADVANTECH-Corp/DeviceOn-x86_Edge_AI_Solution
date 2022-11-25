## Export your model

After a training process is done, click `Performance` tab at the top of current page and you will see `Export` item in this Performance sheet.

<p align="center">
  <img width="600" src="image\12.png">
</p>

>  _**Notice**_ : If you doesn't select `General (compact) [S1]` in the beginning of your project, here `Export` will be gray and unavailable.

<p align="center">
  <img width="600" src="image\13.png">
</p>

>  Image source : https://blog.alantsai.net/posts/2018/08/bot-framework-with-ai-cognitive-service-31-export-custom-vision-trained-model-and-use-dockerfile-to-run-locally#WizKMOutline_1534085309606709

After you click `Export`, a pop-up window shows up. Therein you can see many export types(/frameworks), such as ONNX, TensorFlow, Dockerfile, OpenVino, etc. Then you can choose a target suitable for your application to be exported. In this repo, `Dockerfile` is selected as demonstration.

<p align="center">
  <img width="600" src="image\14.png">
</p>

There are three versions in Dockerfile export: Linux, Windows and ARM (Raspberry Pi 3).

To get a required docker file, select `Linux`, then click `Download` and finally click `Export`.

<p align="center">
  <img width="600" src="image\15.png">
</p>

Afterwards unzip the downloaded file, and the included files are listed as below.

<p align="center">
  <img width="600" src="image\16.png">
</p>

Therein a `Dockerfile` will trigger required actions to pull/download the libraries for AI inference computing.

## Build a docker image including your model

Before you start to execute docker operations, something you must know is how to prepare a docker runtime/environment.

> To install and set up a docker runtime/environment, firstly you can download it [here](https://www.docker.com/products/docker-desktop).

In this repo, there are two examples to create a docker image for AI inference and deployment later.

* With a **Docker file** from Auzre Custom Vision, it actually runs a **TensorFlow model**. One of key reasons to adopt this export type is that it's very convenient and easy to furhter integrate with **Azure IoT Edge** and **Azure ML**.

* Moreover there is another complete example to execute inference with a model of Azure Dockerfile format. It allows you to feed in a video input, show inference results in real time, and output it as a video format.

You can begin with one of them according to your need or interest.

### 1. Dockerfile from Azure Custom Vision
#### Build up a docker image

  1. Open a terminal and move to the directory of the docker file.

  2. Enter the instruction:
  
  ```
    sudo docker build -t <your image name> .
  ```

<p align="center">
  <img width="600" src="image\17.png">
</p>

  3. After it finishes, enter the following instruction, and you can see the image you just have built.

  ```
    sudo docker image ls
  ```

<p align="center">
  <img width="600" src="image\18.png">
</p>

#### Create and run a docker container for image validation

* Enter the instruction:

  ```
    sudo docker run -p 127.0.0.1:80:80 -d --rm <your image name>
  ```

* To check if the docker container is running successfully, launch a web browser and then enter `localhost`, `127.0.0.1:80` or your virtual manchine ip. Finally, we would say it works normally for now if you can see a `CustomVision.ai model host harness` is there.

<p align="center">
  <img width="600" src="image\20.png">
</p>

* You also can use a image file in your device to do a simple test with the following instruction.

  ```
    curl -X POST http://127.0.0.1/image -F imageData=@</.../image_name.jpg, ex:/home/advantech/test_image.jpg>
  ```

* You can see inference result printed in the terminal window.

<p align="center">
  <img width="600" src="image\19.png">
</p>

#### (Optional) Encapsulate a customization docker image from the running container

If you need to customize a docker image, the following commands will be also necessary for you after you put other necessary components or functionalities into the original container.  

> _REMARK_: Keep the container running while executing the command.

* Open a new terminal and check the running container ID, and then enter the following command

```
$ sudo docker commit <container ID> <your image name>
```

( For example: `sudo docker commit 3380f16f9163 advantech_factoryai:v0` )

* After the committing process is completed, type `$ sudo docker image ls` to check if it is successful.

<p align="center">
  <img width="600" src="image\26.png">
</p>

Finally, you can have a new docker image.

### 2. Docker image from Docker Hub
#### Pull a base image
* In order to visualize inference results and use GPU as accelerator to increase performance, openCV and cudnn, which Nvidia GPU card is used, are necessary.
* Enter the following command in terminal
```
$ sudo docker pull datamachines/cudnn_tensorflow_opencv:11.6.2_2.9.1_4.6.0-20220815
```
<p align="center">
  <img width="600" src="image\21.png">
</p>

* After finishing, enter the following command to check if a docker image of `datamachines/cudnn_tensorflow_opencv` exists.
```
$ sudo docker image ls
```

<p align="center">
  <img width="600" src="image\22.png">
</p>

#### Create and run a container with the base image
* Firstly, we start a container to be a base for creating a customization docker image later. 
* In order to automatically launch your own application in the container, you have to copy required files from your local host directory such as `/home/advan/Downloads/azure_docker/app` to a folder of the container that you created. In this repo, I created a folder named `advan` in my container, and there are a model file, .py files, and a video file as inference input in it.
* Enter the following command
```
$ sudo docker run --gpus all -e DISPLAY -e QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix -v <your local directory>:/dmc -it --rm datamachines/cudnn_tensorflow_opencv:11.6.2_2.9.1_4.6.0-20220815 bash 
```

#### Encapsulate a customization docker image from the running container
Make sure you have put all the necessary contents or components into the running container and then just enter the following command.

> _REMARK_: Keep the container running while executing the command.

* Open a new terminal and check the running container ID, and then enter the following command

```
$ sudo docker commit <container ID> <your image name>
```

( For example: `sudo docker commit dc0a9c7dbfcb advantech_edge_ai:v1` )

* After the committing process is completed, type `$ sudo docker image ls` to check if it is successful.

<p align="center">
  <img width="600" src="image\23.png">
</p>

Once a new customization docker image is created successfully, you can delete the base image  `datamachines/cudnn_tensorflow_opencv:11.6.2_2.9.1_4.6.0-20220815` for saving your storage.

#### Create and run a docker container for the customization image validation
* We prepared a shell script as show below, `run_detection.sh`, to run a docker container with the customization image of `advantech_edge_ai:v1`, and also to execute `app_video.py` to show up visualized recognition results.

<run_detection.sh>：
```
#! bash/bash

sudo docker run --gpus all -e DISPLAY -e QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix -v -dt advantech_edge_ai:v1 python ../advan/app_video.py 
```

<p align="center">
  <img width="600" src="image\24.png">
</p>

<p align="center">
  <img width="600" src="image\25.png">
</p>

## Upload your image to ACR (Azure Container Registry)
#### Install WISE-Agent
> We use `WISE-DeviceOn` to simplify this whole procedure, uploading image from your local device to Azure. 
* Registry `WISE-DeviceOn` on http://deviceon.wise-paas.com.

<p align="center">
  <img width="600" src="image\27.png">
</p>

* Setup and onboard ypur linux device with Credential and IoT key, and these will be used when you login `WISE-Agent`.

<p align="center">
  <img width="600" src="image\28.png">
</p>

<p align="center">
  <img width="600" src="image\29.png">
</p>

* Install [WISE-Agent](), which it has two version, Linux and Windows. Since we do this practice in Unbuntu 20.04, `wise-agent-Ubuntu_20.04-x86_64-1.4.45.0.run` is used.

<p align="center">
  <img width="600" src="image\30.png">
</p>

<p align="center">
  <img width="600" src="image\31.png">
</p>

#### Create Container Registry on Azure
* Go to Azure Marketplace and search `container registry`

<p align="center">
  <img width="600" src="image\32.png">
</p>

* Create Container Registry

<p align="center">
  <img width="600" src="image\33.png">
</p>

<p align="center">
  <img width="600" src="image\33_1.png">
</p>

#### Configure ACR into DeviceOn Server
* Access keys

<p align="center">
  <img width="600" src="image\34.png">
</p>

#### Add a registry on WISE-DviceOn
<p align="center">
  <img width="600" src="image\35.png">
</p>

<p align="center">
  <img width="600" src="image\36.png">
</p>

#### Push an image to ACR
* Go back to your linux, and login WISE-DviceOn.

<p align="center">
  <img width="600" src="image\37.png">
</p>
 
* Push your image.
> Use docker tag to create an alias of the image with the fully qualified path, which means the name of alias must include registry url just like our example.

<p align="center">
  <img width="600" src="image\38.png">
</p>




