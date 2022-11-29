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

* Click one of icons where locates red circle to add device for device connection and then you can see the info of both `Credential URL` and `IoT Key`. Both of them are necessary for finishing your WISE-Agent setup later.

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
> Select your registries and click on <i class="fa fa-refresh" aria-hidden="true"></i> icon to synchronize the docker image list to DeviceOn

<p align="center">
  <img width="600" src="image\39.png">
</p>

<p align="center">
  <img width="600" src="image\40.png">
</p>

> Next, the repository and image listing information is displayed on DeviceOn, and you can start deploying these images to edge devices.

<p align="center">
  <img width="600" src="image\41.png">
</p>

#### 2. Open docker dashboard in DeviceOn
* Through the dashboard, DeviceOn provides the summary of device docker status, for example how many container, images, volumes, and networks on that edge device. 
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
  <img width="600" src="image\44.png">
</p>

* Enter the following values: 
- Container name
- Select your source images (from registry or device)
- Select your image
- Configure the container running parameters, such as port mapping, or specific command

* Then, you could decide the container run automatically or manually start later. BTW, for batch deploy container, you may switch to "**Group Mode**" to select which device group need to run the container.

* In the beginning, it is recommended that you deploy the container to a device to make sure everything, configuration works, and then batch provisioning.

<p align="center">
  <img width="600" src="image\45.png">
</p>

<p align="center">
  <img width="600" src="image\46.png">
</p>

#### 4. Run your container at edge
# (待換圖)
> If you do not enable "**Auto Start**" on add container step, the default image state will be **Created** not **Running**. Please select the container and click on <i class="fa solid fa-play"></i> icon to run the container.

<p align="center">
  <img width="600" src="https://i.imgur.com/4b1heFK.png">
</p>

You will see the container is remotely launched to execute inference at your edge.

<p align="center">
  <img width="600" src="image\25.png">
</p>

...

# (以下 參考資料 from Sephi，待重整)
# Operation - Deploy AI to Edge Device

- [Operation - Deploy AI to Edge Device](#operation---deploy-ai-to-edge-device)
  * [Purpose](#purpose)
  * [Prerequisites](#prerequisites)
  * [Step 1: Onboarding Your Device to IoT Device Platform (DeviceOn)](#step-1--onboarding-your-device-to-iot-device-platform--deviceon-)
    + [1. Log in to the DeviceOn Cloud Service with Your Account and Password](#1-log-in-to-the-deviceon-cloud-service-with-your-account-and-password)
    + [2. Download WISE-Agent and Setup on your Device](#2-download-wise-agent-and-setup-on-your-device)
    + [3. Open a terminal](#3-open-a-terminal)
    + [4. Copy the installer to target host](#4-copy-the-installer-to-target-host)
    + [5. Set the installer as executable](#5-set-the-installer-as-executable)
    + [6. Running the installer](#6-running-the-installer)
    + [7. Start WISE-Agent and Connect to DeviceOn](#7-start-wise-agent-and-connect-to-deviceon)
    + [8. Start Device Management](#8-start-device-management)
  * [Step 2: Enalbe and Configure Azure Container Registry on DeviceOn](#step-2--enalbe-and-configure-azure-container-registry-on-deviceon)
    + [1. Configure Container Registry](#1-configure-container-registry)
    + [2. Synchronize Registry](#2-synchronize-registry)
  * [Step 3: Deploy a Container to Edge Device through DeviceOn](#step-3--deploy-a-container-to-edge-device-through-deviceon)
    + [1. Docker Dashboard](#1-docker-dashboard)
    + [2. Deploy a Container to Edge Device](#2-deploy-a-container-to-edge-device)
    + [3. Run Container](#3-run-container)


Purpose
---
Through the IoT device platform called DeviceOn to provides containers management to help AI developer or system opterator to batch provision inference container to edge devices. DeviceOn is the best platform not only manage contaienr but application. In the section, we would like to focus on how to deploy container to edge devices.


Prerequisites
---
- A workable DeviceOn server must be installed and running without problems. You could refer to the [documentation](https://docs.wise-paas.advantech.com/en/Guides_and_API_References/ApplicationServices/1564727799415968385/1589506780729736622/v1.0.0) of DeviceOn to set up your own server.
- An edge device for Ubuntu Linux 18.04/20.04 ready.
- An Azrue Container Regiesty created.

#### If your platform is Ubuntu 18.04 on *Nvidia Jetson*, please execute the following commands to install the dependent libraries.

1. To download package information from all configured sources:
```
sudo apt update
```
2. To install the dependent libraries:
```
sudo apt install cmake curl libxml2 libx11-6 libxext6 libxtst6 libmosquitto1 sqlite3 xterm ethtool lua5.1 net-tools openssl libcurl4 gcc g++ make cmake libxml2-dev libx11-dev libxtst-dev libxext-dev libmosquitto-dev autoconf autotools-dev build-essential libtool zlib1g-dev libcurl4-openssl-dev libssl-dev -y
```

Step 1: Onboarding Your Device to IoT Device Platform (DeviceOn)
---
Once your DeviceOn server installed, you could start to follow steps to onboarding your edge device.

 ### 1. Log in to the DeviceOn Cloud Service with Your Account and Password

![](https://i.imgur.com/cs5FCGe.png)

 ### 2. Download WISE-Agent and Setup on your Device
> Please try to get and download the latest version of [WISE-Agent installer](https://eiot.blob.core.windows.net/deviceon/WISE-Agent.zip) for Linux version from [technical portl](https://docs.wise-paas.advantech.com/en/Guides_and_API_References/ApplicationServices/1564727799415968385/1564727878040194797/v1.0.2) or [landing page](https://campaign.advantech.online/en/DeviceOn/index.html).

 ### 3. Open a terminal

>The installer runs in CLI (Command Line Interface) mode. As such, open a terminal preferable for you.

 ### 4. Copy the installer to target host

>Use the way you like to copy the installer to the target host.

 ### 5. Set the installer as executable

>In the terminal, run “**chmod 0755 wise-agent-Ubuntu 18.04 x86_64-1.x.x.0.run**” so that the installer as an executable file under Ubuntu Linux.

![](https://i.imgur.com/QFAf258.png)

 ### 6. Running the installer
 
> Change your working directory to where the installer is and run "**./wise-agent-Ubuntu 18.04 x86_64-1.x.x.0.run**". You may need to run "**sudo ./wise-agent-Ubuntu 18.04 x86_64-1.x.x.0.run**" to acquire higher privileges if you were logged in as a normal user.

![](https://i.imgur.com/gU7Dxvu.png)


 ### 7. Start WISE-Agent and Connect to DeviceOn
 
> Change your directory to /usr/local/AgentService and run sudo ./setup.sh to answer connection information, such as credential URL, IoTKey, Device Name and etc.

![](https://i.imgur.com/DfOk1Vz.png)

* Zero-touch onboard is a zero-configuration and quick connection mode for a special purpose. The default is disabled (n).
* Enter Credential URL and IoT Key that information could retrieve from the DeviceOn portal.

![](https://i.imgur.com/JkQLu2M.png)


* Assign device to User Account: You can bind the target device into a “Default” group in your account on the portal automatically.
* Enable TLS: Turn ON/OFF the TLS/SSL mode.
* Input Device Name: Give your device name and show it on the portal.
* Input AMT ID and password: If your device support Intel AMT, please enter AMT ID and Password to enable these functions.
* Select KVM Mode [0:default, 1:Custom VNC, 2:disable]: User can use our default VNC to support the Remote Desktop function by entering 0 and give a listen port if you don’t want to use the default port. Second, select Custom Mode, if they already have a VNC server by entering 1 and provide the listen port and password. To disable the KVM function by entering 2.

> When you run into this step the question shows like above, device is connected and under your account

 ### 8. Start Device Management

> By default, two “Real-time Actions” are created for a group, one is “Screenshot” and the other one is “Reboot”. The overview page further shows the online status of registered.

![](https://i.imgur.com/30uFMjk.png)


Step 2: Enable and Configure Azure Container Registry on DeviceOn
---

### 1. Configure Container Registry

> Go to Container -> Registries and click "**+**" icon to add regiscty for your docker image. DeviceOn supports Azure Container Registry (ACR) as public registry and Harbor for private. Here we take ACR as an example, you could find releated information from ACR, such as, Registry URL, User and Token (Password).

![](https://i.imgur.com/CoQ8trG.png)

![](https://i.imgur.com/8NGrIOd.png)


### 2. Synchronize Registry

> Select your registries and click on <i class="fa fa-refresh" aria-hidden="true"></i> icon to synchronize the docker image list to DeviceOn

![](https://i.imgur.com/kqSVM8m.png)

> Next, the repository and image listing information is displayed on DeviceOn, and you can start deploying these images to edge devices.

![](https://i.imgur.com/h1Mu8w3.png)


Step 3: Deploy a Container to Edge Device through DeviceOn
---

### 1. Docker Dashboard

> Through the dashboard, DeviceOn provides the summary of device docker status, for example how many container, images, volumes, and networks on that edge device. 

![](https://i.imgur.com/9eizMng.png)

> Click on the **Containers** to shows details.

![](https://i.imgur.com/8QZYdH1.png)


### 2. Deploy a Container to Edge Device

> Click "**+**" icon to deploy a new container from your registry that we configured on Step 2.

![](https://i.imgur.com/fcmGcE6.png)

> Enter the following values: 
- Container name
- Select your source images (from registry or device)
- Select your image
- Configure the container running parameters, such as port mapping, or specific command

> Then, you could decide the container run automatically or manually start later. BTW, for batch deploy container, you may switch to "**Group Mode**" to select which device group need to run the container.

> In the beginning, it is recommended that you deploy the container to a device to make sure everything, configuration works, and then batch provisioning.

![](https://i.imgur.com/NOLzt20.png)


### 3. Run Container

> If you do not enable "**Auto Start**" on add container step, the default image state will be **Created** not **Running**. Please select the container and click on <i class="fa solid fa-play"></i> icon to run the container.

![](https://i.imgur.com/4b1heFK.png)

You will see the container is remotely launched to execute inference.

<p align="center">
  <img width="600" src="image\25.png">
</p>

