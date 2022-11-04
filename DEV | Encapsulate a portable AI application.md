## Export your model

As you decide to apply the model you have trained, click `Performance` in the top of your page, and you will see `Export` under Performance tab.

<p align="center">
  <img width="600" src="image\12.png">
</p>

>  _**Notice**_ : If you didn't pick `General (compact) [S1]` at the first time you created your project, `Export` will be gray and can't be used.

<p align="center">
  <img width="600" src="image\13.png">
</p>

from : https://blog.alantsai.net/posts/2018/08/bot-framework-with-ai-cognitive-service-31-export-custom-vision-trained-model-and-use-dockerfile-to-run-locally#WizKMOutline_1534085309606709

After you push `Export`, it will show a pop-up window, and you can see many platforms, such as ONNX, TensorFlow, Dockerfile, OpenVino, etc. Then you can choose one platform that is suitable of your application. For this practice, `Dockerfile` would be selected.

<p align="center">
  <img width="600" src="image\14.png">
</p>

There are three version, Linux, Windows, and ARM (Raspberry Pi 3), in Dockerfile platform.

Select `Linux`, push `Download` and then click `Export`.

<p align="center">
  <img width="600" src="image\15.png">
</p>

Unzip the downloaded file, and it would be like below

<p align="center">
  <img width="600" src="image\16.png">
</p>

## Use Docker file

> If you don't have docker yet, you could download it from [here](https://www.docker.com/products/docker-desktop).

In this **Docker file**, it actually runs **TensorFlow's model**. The crucial reason to use this platform is that it's very convenient and easy to integrate with **Azure IoT Edge** and **Azure ML**.

Let's build up the **Docker Image** first.

##### Build up the Docker Image

* Open a terminal and move to the directory of the docker file.

  [image17]()

* Enter the instruction:

  ```
  sudo docker build -t <your image name> .
  ```

* After it finishes, Enter the following instruction, and you can see the image you just have built.

  ```
  sudo docker image ls
  ```

  [image18]()

##### Run test

* Enter the instruction:

  ```
  sudo docker run -p 127.0.0.1:80:80 -d --rm <your image name>
  ```

* Go to explorer, and enter `localhost`. You will see `CustomVision.ai model host harness`.

  [image19]()

* You also can use the images in your computer to do this test by enter the following instruction.

  ```
  curl -X POST http://127.0.0.1/image -F imageData=@<your_image_name.jpg, ex:/home/advantech/test_image.jpg>
  ```

* The result will be like

  [image20]() 



