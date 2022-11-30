Purpose
---
Through the IoT device platform called `DeviceOn` to provide containers management to help AI developer or system opterator to batch provision inference container to edge devices. 'DeviceOn' is the best platform not only manage contaienr but application. In the section, we would like to focus on how to deploy your container to edge devices and furhter remotely controll it through `DeviceOn`.

Prerequisites
---
- A workable [DeviceOn server](https://eiot.blob.core.windows.net/deviceon/DeviceOn_Server.zip) must be installed and running without problems. You could refer to the [documentation](https://docs.wise-paas.advantech.com/en/Guides_and_API_References/ApplicationServices/1564727799415968385/1589506780729736622/v1.0.0) of DeviceOn to set up your own server.
- [A 90-day trial key](https://www.youtube.com/watch?v=tjZUchu0v2I&t=64s) for DeviceOn server activation.
- EPC-B5587 with Linux [Ubuntu 20.04](https://campaign.advantech.online/en/embedded_software/index.html) ready.

## Connect your device to DeviceOn server

> In this repo, we used `DeviceOn` to simplify and accelerate the whole pipelie of edge AI development and deployment.

#### 1. Install WISE-Agent in your AI device

* Install [WISE-Agent](https://eiot.blob.core.windows.net/deviceon/WISE-Agent.zip) with the file of `wise-agent-Ubuntu_20.04-x86_64-1.4.45.0.run` therein for Unbuntu 20.04 that we implemented in this repo.

<p align="center">
  <img width="600" src="image\30.png">
</p>

<p align="center">
  <img width="600" src="image\31.png">
</p>

> The details of configurations in above picture are shown in the 3rd step.

#### 2. Login your DeviceOn portal to get connection info

* Open your `DeviceOn` portal with a web brwoser.

<p align="center">
  <img width="600" src="image\27.png">
</p>

* Click the right-top icon with a red circle to add device (connection) for the first time, and then you can see the info of both `Credential URL` and `IoT Key`. Both of them are necessary for finishing your WISE-Agent setup later.

<p align="center">
  <img width="600" src="image\28.png">
</p>

<p align="center">
  <img width="600" src="image\29.png">
</p>

> Please note that keep or save `Credential URL` and `IoT Key` for setting up WISE-Agnet.

#### 3. Connect your device with WISE-Agent to the DeviceOn server
* Turn on a terminal on your device.
* Change your directory to `/usr/local/AgentService` and run sudo `./setup.sh` to answer connection information, such as credential URL, IoTKey, Device Name and etc. After finishing these, it will make your device accessible for all (or specific) DeviceOn accounts.

<p align="center">
  <img width="600" src="image\31.png">
</p>

> Remark
> * `Zero-touch onboard` is a zero-configuration and quick connection mode for a special purpose. The default is disabled (n).
> * Enter `Credential URL` and `IoT Key` that information could retrieve from the DeviceOn portal.
> * `Assign device to User Account`: You can bind the target device into a `Default` group in your account on the portal automatically.
> * Enable `TLS`: Turn ON/OFF the TLS/SSL mode.
> * Input `Device Name`: Give your device name and show it on the portal.
> * Input `AMT ID and password`: If your device support Intel AMT, please enter AMT ID and Password to enable these functions.
> * Select `KVM Mode` [0:default, 1:Custom VNC, 2:disable]: User can use our default VNC to support the Remote Desktop function by entering 0 and give a listen port if you don’t want to use the default port. Second, select Custom Mode, if they already have a VNC server by entering 1 and provide the listen port and password. To disable the KVM function by entering 2.

## Set an ACR connection in DeviceOn
#### Add a registry for ACR in DeviceOn

* Click the `Container | Registry` and then the icon of `+`. 

<p align="center">
  <img width="600" src="image\35.png">
</p>

* Fill in the necessary infomation referred to the `Access keys` in `Settings` of  your ACR page.

* Therein `Token` in DeviceOn means the 1st-row `password` in ACR.

<p align="center">
  <img width="600" src="image\36.png">
</p>

<p align="center">
  <img width="600" src="image\34.png">
</p>

* Then press `Confirm` to complete this ACR connection with DeviceOn. 

## Manipulate container deployment from ACR to AI edge(s) through DeviceOn 
#### 1. Synchronize Registry
* Select your registries and click on <i class="fa fa-refresh" aria-hidden="true"></i> icon to synchronize the docker image list to DeviceOn

<p align="center">
  <img width="600" src="image\39.png">
</p>

<p align="center">
  <img width="600" src="image\40.png">
</p>

* Next, the repository and image listing information is displayed on DeviceOn, and you can start deploying these images to edge devices.

<p align="center">
  <img width="600" src="image\41.png">
</p>

#### 2. Open docker dashboard in DeviceOn
* Through the dashboard, DeviceOn provides the summary of device docker status, for example how many containers, images, volumes, and networks on that edge device. 
* Click on the **Containers** to shows details.

<p align="center">
  <img width="600" src="image\42.png">
</p>

<p align="center">
  <img width="600" src="image\43.png">
</p>

#### 3. Deploy a container to edge device
* Click "**+**" icon to deploy a new container from your registry that we configured on Step 2.

<p align="center">
  <img width="600" src="image\45.png">
</p>

* Enter the following values: 
  - Container name
  - Select your source images (from registry or device)
  - Select your image
  - Configure the container running parameters, such as port mapping, or specific command

* Then, you could decide the container run automatically or manually start later. BTW, for batch deploy container, you may switch to "**Group Mode**" to select which device group need to run the container.

* For automatically activating object detetion, the most important thing is to set a proper docker api in `Advanced Mode` of `Container Settings`. [Here](https://github.com/ADVANTECH-Corp/DeviceOn-x86_Edge_AI_Solution/blob/main/sample%20codes/autorun_cmd.txt) is a example for this practice.

<p align="center">
  <img width="600" src="image\46.png">
</p>

> In the beginning, it is recommended that you deploy the container to a device to make sure everything, configuration works, and then batch provisioning.

#### 4. Run your container at edge
* If you do not enable "**Auto Start**" on add container step, the default image state will be **Created** not **Running**. Please select the container and click on <i class="fa solid fa-play"></i> icon to run the container.

<p align="center">
  <img width="600" src="image\47.png">
</p>

<p align="center">
  <img width="600" src="image\48.png">
</p>

* You will see the container is remotely launched to execute inference at your edge.

<p align="center">
  <img width="600" src="image\25.png">
</p>
