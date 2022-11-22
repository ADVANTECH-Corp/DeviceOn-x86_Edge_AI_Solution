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

Afterwards unzip the downloaded file, and it would be like as below.

<p align="center">
  <img width="600" src="image\16.png">
</p>

Therein the `Dockerfile` in the unzipped directory includes required actions to pull/download the libraries for AI inference computing.

## Use Docker file

> To install and set up a docker runtime/environment, firstly you can download it [here](https://www.docker.com/products/docker-desktop).

* With the **Docker file**, it actually runs a **TensorFlow model**. One key reason to adopt this export type is that it's very convenient and easy to furhter integrate with **Azure IoT Edge** and **Azure ML**.
* There is a more flexible way to execute the inference with the model of Azure Dockerfile format, and this way allows you to fed in video input, show the result in real-time, and save it as a video format. You can decide one of the two methods according your need.

### 1. Azure Custom Vision's dockerfile
#### Build up a Docker image

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

#### Create and run a Docker container

1. Enter the instruction:

  ```
    sudo docker run -p 127.0.0.1:80:80 -d --rm <your image name>
  ```

2. To check if the docker container is running successfully, launch a web browser and then enter `localhost`, `127.0.0.1:80` or your virtual manchine ip. Finally, we would say it works normally for now if you can see a `CustomVision.ai model host harness` is there.

<p align="center">
  <img width="600" src="image\20.png">
</p>

3. You also can use a image file in your device to do a simple test with the following instruction.

  ```
    curl -X POST http://127.0.0.1/image -F imageData=@</.../image_name.jpg, ex:/home/advantech/test_image.jpg>
  ```

4. Finally you can see inference result printed in the terminal window.

<p align="center">
  <img width="600" src="image\19.png">
</p>

### 2. Custom docker image
#### Pull docker image
* In order to display the result and use GPU to increase the performance, openCV and cudnn, which GeForce GTX 1650 is used, are necessary.
* Enter the following command in terminal
```
$ sudo docker pull datamachines/cudnn_tensorflow_opencv:11.6.2_2.9.1_4.6.0-20220815
```
<p align="center">
  <img width="600" src="image\21.png">
</p>

* After finishing, enter the following command to check if the image is existed. If it is, `datamachines/cudnn_tensorflow_opencv` will be shown.
```
$ sudo docker image ls
```

<p align="center">
  <img width="600" src="image\22.png">
</p>

#### Run a image as a container
* First, we start a container to be a base for create a custom image
* In order to run the container and automatically activate your own application, you have to copy files from your local directory such as `/home/advan/Downloads/azure_docker/app` to a folder of the container you create. In this demo, I create a folder named `advan` in my container, and there are model file, .py files, and a video in it.
* Enter the following command
```
$ sudo docker run --gpus all -e DISPLAY -e QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix -v <your local directory>:/dmc -it --rm datamachines/cudnn_tensorflow_opencv:11.6.2_2.9.1_4.6.0-20220815 bash 
```
> _REMARK_: Keep the container alive.

#### Create a image from a container
* Make sure you have updated the contents of the running container and just enter the following command.

```
$ sudo docker commit advantech_edge_ai:v1
```
* After committing your container, type `$ sudo docker image ls` to check if it is successful.
* 
<p align="center">
  <img width="600" src="image\23.png">
</p>

> After it successes, you can delete the base image, `datamachines/cudnn_tensorflow_opencv:11.6.2_2.9.1_4.6.0-20220815`.

#### Run the new image
* We wrote a shell script to run the new image and automatically execute `app_video.py` to display online detection result.

<p align="center">
  <img width="600" src="image\25.png">
</p>


# !!!(待補) 另一個完整的打包方式

1包cotainer image，包括AI app, inference data, inference server, AI model, ...
(之後進版時，再整理比較合理的作法：2包container images，1包主要是AI app + inference data；另1包主要是inference server + AI model。)
