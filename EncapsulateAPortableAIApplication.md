## Export your model

After a training process is done, click `Performance` tab at the top of current page and you will see `Export` item in this Performance sheet.

<p align="center">
  <img width="600" src="image\12.png">
</p>

>  _**Notice**_ : If you doesn't select `General (compact) [S1]` in the beginning of your project, here `Export` will be gray and unavailable.

<p align="center">
  <img width="600" src="image\13.png">
</p>

After you click `Export`, a pop-up window shows up. Therein you can see many export types(/frameworks), such as ONNX, TensorFlow, Dockerfile, OpenVino, etc. Then you can choose a target suitable for your application to be exported. In this practice, `Dockerfile` is selected as demonstration.

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

The environment of the following operation is in ubuntu 20.04.

> To install and set up a docker runtime/environment, firstly you can download it [here](https://www.docker.com/products/docker-desktop).

In this repo, there are two examples to create a docker image for AI inference and deployment later.

* One of crucial reasons to use this export type is that it's very convenient and easy to furhter integrate with Azure IoT Edge and Azure ML.

* Moreover there is another example, **creating a customization docker image**, to execute inference with an AI model in the `app` directory from [the downloaded file of Dockerfile option](/image/16.png). It allows you to feed in a video input, show inference results in real time, and output it as a video format.

The following is 2 different applications, and you can begin with one of them according to your need or interest.

### 1. Dockerfile from Azure Custom Vision
#### Build up a docker image

  1. Open a terminal and move to the directory of the docker file.

  2. Enter the instruction:
  
  ```
    sudo docker build -t <your image name> .
  ```
  > NOTICE: make sure that your image name must be lower case

<p align="center">
  <img width="600" src="image\17.png">
</p>

<p align="center">
  <img width="600" src="image\17-1.png">
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

* To check if the docker container is running successfully, launch a web browser and then enter `localhost`, `127.0.0.1:80`. Finally, we would say it works normally for now if you can see a `CustomVision.ai model host harness` is there.

<p align="center">
  <img width="600" src="image\20.png">
</p>

* You also can use a image file in your device to do a simple test with the following instruction.

  ```
    curl -X POST http://127.0.0.1/image -F imageData=@<your image path>
  ```

* You can see inference result printed in the terminal window.

<p align="center">
  <img width="600" src="image\19.png">
</p>

#### (Additional) Encapsulate a customization docker image from the running container

If you need to customize a docker image, the following commands will be also necessary for you after you put other necessary components or functionalities into the original container.  

> REMARK: Keep the container running while executing the command.

* Open a new terminal and check the running container ID, and then enter the following command

```
$ sudo docker commit <container ID> <your image name>
```

( For example: `sudo docker commit 3380f16f9163 advantech_factoryai:v0` )

> Enter `sudo docker ps -l`, and then you can check the container ID

* After the committing process is completed, type `$ sudo docker image ls` to check if it is successful.

<p align="center">
  <img width="600" src="image\26.png">
</p>

Finally, you have created a new docker image.

### 2. Docker image from Docker Hub
#### Pull a base image
* In order to visualize inference results and use GPU as accelerator to increase performance, openCV and cudnn, which Nvidia GPU card is used, are necessary.
* Enter the following command in terminal
```
$ sudo docker pull datamachines/cudnn_tensorflow_opencv:11.6.2_2.9.1_4.6.0-20220815
```
> There may be other version, and you can find it in this [web page](https://hub.docker.com/r/datamachines/cudnn_tensorflow_opencv) in dockerhub.

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

#### Prepare required files for creating a customization docker image
* Download required files from [here](/advan) to your local directory, and make sure that you have put all the necessary contents or components into the directory.

#### Create and run a container with the base image
* Enter the following command, and `your local directory` is the directory where you saved the required files.

```
$ sudo docker run -v <your local directory>:/advan -it --rm datamachines/cudnn_tensorflow_opencv:11.6.2_2.9.1_4.6.0-20220815 bash 
```

#### Encapsulate a customization docker image from the running container

> REMARK: Keep the container running.

* Open a new terminal and check the running container ID, and then enter the following command

```
$ sudo docker commit <container ID> <your image name>
```

( For example: `sudo docker commit dc0a9c7dbfcb advantech_edge_ai:v1` )

> Enter `sudo docker ps -l`, and then you can check the container ID

* After the committing process is completed, type `$ sudo docker image ls` to check if it is successful.

<p align="center">
  <img width="600" src="image\23.png">
</p>

#### Create and run a docker container for the customization image validation
* We prepared a shell script as show below, `run_detection.sh`, to run a docker container with the customization image of `advantech_edge_ai:v1`, and also to execute `app_video.py` to show up visualized recognition results.

<run_detection.sh>：
```
#!/bash/bash

sudo docker run --gpus all -e DISPLAY=:0.0 -e QT_X11_NO_MITSHM=1 --net=host -v /tmp/.X11-unix:/tmp/.X11-unix -dt <your image name> python app_video.py
```

<p align="center">
  <img width="600" src="image\24.png">
</p>

<p align="center">
  <img width="600" src="image\25.png">
</p>

## Upload your docker image to ACR (Azure Container Registry)
In this repo, we will use ADVANTECH DeviceOn to simplify and accelerate you AI deployment at scale.For your containerized AI, we can use ACR as an interface to make DevcieOn accessible to your docker images. Let's see how to set up your ACR and then push your docker image onto ACR for further deployment by DeviceOn.

> Here is a video for creating an Azure Container Registry to store your container images.
> 
> https://www.youtube.com/watch?v=KAZJlm3aVQw#t=111s

#### Set up your ACR (Azure Container Registry)
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

#### Push an docker image to ACR
* Get the ACR access key

Click `Access keys` in `Settings` of  your ACR page.
Here are necessary information for an ACR configuration in DeviceOn. 

<p align="center">
  <img width="600" src="image\34.png">
</p>

* Login your ACR with the above-mentioned connection info in your build machine.

```
$ sudo docker login <your registry URL>
```

<p align="center">
  <img width="600" src="image\37.png">
</p>
 
* Upload your docker image to ACR.
> Use docker tag to create an alias of the image with the fully qualified path, which means an alias name must include registry url, just like our example.

```
$ sudo docker push <registry URL>
```

<p align="center">
  <img width="600" src="image\38.png">
</p>
