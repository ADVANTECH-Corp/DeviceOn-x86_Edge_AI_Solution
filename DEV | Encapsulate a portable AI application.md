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

With the **Docker file**, it actually runs a **TensorFlow model**. One key reason to adopt this export type is that it's very convenient and easy to furhter integrate with **Azure IoT Edge** and **Azure ML**.

Now let's start to build up a **Docker Image** firstly.

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

# 11/21 Memo with MW

理想又合理的作法：2包container images，1包主要是AI app + inference data；另1包主要是inference server + AI model。
方便demo說明的作法：1包cotainer image，包括AI app, inference data, inference server, AI model, ...
