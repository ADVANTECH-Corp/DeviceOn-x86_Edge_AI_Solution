# Operation - Monitor and Manage Large-scale Devices

- [Operation - Monitor and Manage Large-scale Devices](#operation---monitor-and-manage-large-scale-devices)
  * [Prerequisites](#prerequisites)
  * [How to Manage lots of Devices?](#how-to-manage-lots-of-devices)
    + [Onboarding Devices](#onboarding-devices)
      - [1. Auto Provisioning and Onboarding](#1-auto-provisioning-and-onboarding)
      - [2. One-by-One or Local Provisioning](#2-one-by-one-or-local-provisioning)
    + [On-premise and Cloud Deployment](#on-premise-and-cloud-deployment)
      - [1. On-premise (Standaone Version, 1k Devices)](#1-on-premise-standaone-version-1k-devices)
      - [2. Enterprise (10k+ Devices)](#2-enterprise-10k-devices)
  * [What's the Major Features and How to Do the Remote Control?](#whats-the-major-features-and-how-to-do-the-remote-control)
      - [1. Application Management](#1-application-management)
      - [2. Container Management](#2-container-management)
      - [3. Remote Diagnostic (RDP, Terminal, Screenshot)](#3-remote-diagnostic-rdp-terminal-screenshot)
      - [4. Secure Lockdown Control](#4-secure-lockdown-control)
      - [5. Hardware Management (SUSI)](#5-hardware-management-susi)
      - [6. OOB (Out-of-Band) Managment](#6-oob-out-of-band-managment)
      - [7. Monitoring](#7-monitoring)
  * [What the benefit of using the DeviceOn?](#what-the-benefit-of-using-the-deviceon)
    + [Batch Deployment (App and Container) and Operation](#batch-deployment-app-and-container-and-operation)
    + [Remote Troubleshooting - Inband and OOB](#remote-troubleshooting---inband-and-oob)
    + [Data acquisition and Visualization](#data-acquisition-and-visualization)

Prerequisites
---

- A workable DeviceOn server must be installed and running without problems. You could refer to the [documentation](https://docs.wise-paas.advantech.com/en/Guides_and_API_References/ApplicationServices/1564727799415968385/1589506780729736622/v1.0.0) of DeviceOn to set up your own server.
- An edge device for Windows or Ubuntu Linux 18.04/20.04 ready.


How to Manage lots of Devices?
---

### Onboarding Devices
#### 1. Auto Provisioning and Onboarding

The solution that we integrate on DeviceOn for Azure (Enterprise Edition), leverage **Azure IoT Edge**, **Device Provisioning Service** and **TPM 2.0** to offer secure authentication and private key protected. In the solution could save a lot of time when the deploying amount of the device at one time. The end-user simply open the box and plug-in the power, the device will onboarding to cloud automatically.

TPM, also known as [ISO/IEC 11889](https://www.iso.org/standard/66510.html), is a standard for securely generating and storing cryptographic keys. TPM also refers to a virtual or physical I/O device that interacts with modules that implement the standard. A TPM device can exist as discrete hardware, integrated hardware, a firmware-based module, or a software-based module.

![](https://i.imgur.com/dW4wnGq.png)

#### 2. One-by-One or Local Provisioning

Also, you could reference before section to configure **connection string** and **IoT Key** for each devices. If your device on the same network and firewall allowed for muticast protocol, we have local provisioning tool for user to discover the local devices and transmit the connection information let the devices to onboarding specific cloud.

![](https://i.imgur.com/agP5qWh.png)

### On-premise and Cloud Deployment
DeviceOn is based on microservice design, each conponent is statless and supports mutiple instances for scale up. This result in heavily simplfied deployment to kubernetes, standalone virtual machines. Both public cloud and private (on-premise) deployment are supported.

#### 1. On-premise (Standaone Version, 1k Devices)

The standalone version provides all packages of the DeviceOn software in one installer package, including RabbitMQ as a message broker, MongoDB, PostgreSQL as databases, Grafana for visualization, Tomcat for web services, and a watchdog service that protects DeviceOn core components from crashing or becoming unresponsive.

To achieve a more satisfying experience with DeviceOn, particularly in terms of the client software, it is highly recommended that your system be substantially better than the minimum requirements specified in the following sections

Attention to the following areas can make a significant improvement to your overall user experience and enjoyment of the software:

* **Intel® Core™ i5 2.3 GHz CPU and at least 8GB of RAM**
* **25 GB root partition for the system**
* **100 GB data storage partition (for documents and indexing)**

General Operation Systems and Recommendations:

* **Windows Server 2016 64-bits**
* **Windows Server 2019 64-bits**
* **Windows Server 2022 64-bits**
* **Ubuntu 18.04/20.04 64-bits**

>[Download Installer <i class="fa solid fa-download"></i>](https://eiot.blob.core.windows.net/deviceon/DeviceOn_Server.zip)

#### 2. Enterprise (10k+ Devices)
The Azure Kubernetes Service (AKS) makes it easy to deploy a managed Kubernetes cluster to Azure. AKS reduces the complexity and operational overhead of managing Kubernetes by offloading much of that responsibility to Azure. Azure handles critical tasks like health monitoring and maintenance for those Kubernetes services.

Deploying DeviceOn on the Azure Kubernetes Service is easy and with just a few steps, containers or nodes can be scaled up to manage 10 thousands of devices. Moreover, DeviceOn can leverage the Azure IoTHub and Cosmos DB for Azure native security and performance. Since the data is already stored on the Azure cloud, it is much easier to leverage the Azure ecosystem – for example using the provided data for Azure Machine Learning.

>[Deploy to Azure <i class="fa duotone fa-play"></i>](https://portal.azure.com/#create/Microsoft.Template/uri/https%3a%2f%2fmarketplacetemplate.blob.core.windows.net%2fdeviceon%2fDeviceOn.json)

![](https://i.imgur.com/DHB0qrY.png)

What's the Major Features and How to Do the Remote Control?
---
#### 1. Application Management
OTA supports an open framework, which can easily integrate 3rd party storage, such as FTP and cloud solutions (Azure Blob, AWS S3, AliYun, Openstack Swift). It does not only support remote update and deployment, but supports automatic update from server side as well as scheduled updates that get triggered from the agent side. Scheduling helps to avoid peak network traffic times and allows implementation of download and deployment schemes that reduce potential impact to a minimum. Scripting support (shell/batch) allows to implement flexible update mechanisms.

![](https://i.imgur.com/NTO7F2J.png)

This video guides you how to accomplish upload and wrap your application to on-premise App Store. And, after the lab, you should:
* Learn how to wrap your software for remote provisioning.
* Have the Notepad++, a popular and famous text editor, populated within the target device.

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1665992238/video_to_markdown/images/youtube--ltdo3xhLNzE-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/ltdo3xhLNzE "")

#### 2. Container Management
Device container management is one of the major feature, you can easily set up, deploy, monitor, and manage each container on different devices. For device managers, it can create, manage and set the health of containers within minutes, and provide a variety of container restart strategies. Through the dashboard, you can quickly understand the running status of the container in the managed device. In addition, for container developers, the Azure Container Repository is supported as a public cloud solution, and private cloud uses Harbor as a container repository.

![](https://i.imgur.com/aTWiBCY.png)

The device management platform (WISE-DeviceOn) launched by Advantech has fully supported the AIR-020 NVIDA Jetson system, and could directly monitor, operate, and deploy AI Inference containers through the container management interface.

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1665992515/video_to_markdown/images/youtube--bilP6FpyU0M-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/bilP6FpyU0M "")

#### 3. Remote Diagnostic (RDP, Terminal, Screenshot)

Provides remote control mechanism, such as KVM (Remote Keyboard-Video-Mouse) for real-time, end-to-end encrypted remote desktop access to the devices. The screenshot functionality allows to capture the device’s current screen output for potential troubleshooting. Another feature is access to Windows or Linux shells, for example in order to quickly retrieve network status via ipconfig/ifconfig, netstat to dump socket/TCP/UDP information, without having to use the full graphical user interface.

#### 4. Secure Lockdown Control

For others features depend on your device operation system and hardware. DeviceOn integrate Windows Lockdown features on LTSC (Long Time Service Channel) and LTSB (Long Time Service Branch) to provide advanced control, such as “**Block USB Drives**”, “**Keyboard Filter**”, **“Block Windows Notification**”, “**Block Touch, Gesture**” and “**UWF (Unified Write Filter)**”. 

* **USB Drive**: Prevent threats from outside USB drives, not include keyboard, mouse.
* **Function Key**: Disables Ctrl, Alt, and WinKey.
* **Windows Notification**: Block application notification. 
* **Touch Screen**: Disable touch control
* **Tough Gesture**: Disable gesture control
* **UWF Protection**: To protect your drives by intercepting and redirecting any writes to the drive (app installations, settings changes, saved data) to a virtual overlay. The virtual overlay is a temporary location that is usually cleared during a reboot or when a guest user logs off.

**Benefits:**
>Provides a clean experience for thin clients and workspaces that have frequent guests, like school, library or hotel computers. Guests can work, change settings, and install software. After the device reboots, the next guest receives a clean experience.

>Increases security and reliability for kiosks, IoT-embedded devices, or other devices where new apps are not expected to be frequently added.

>Can be used to reduce wear on solid-state drives and other write-sensitive media.

#### 5. Hardware Management (SUSI)

For **backlight**, **brightness**, **GPIO** and **Watchdog** only support on Advantech hardware platform with SUSI driver, please download from [Advantech Support](https://support.advantech.com/) site.

![](https://i.imgur.com/fEGfTSS.png)


* **LVDS, Backlight and Brightness**: Turn on/off LVDS backlight for power saving.
* **On Screen Display**: Adjust monitor (brightness, color temperature, resolution, …etc.), especially support on Advantech Industrial Display.
* **Watchdog Protection**: Hardware level watchdog to prevent BSoD (Blue Screen of Death) or system hang without any response. If happened, watchdog will restart your device automatically. There is an tool called NotMyFault that you can use to crash, hang, and cause kernel memory leaks on your Windows system.

**Benefits:** 
> Avoid embarrassing moment, if BSoD on your Signage devices over the airport, department store and public area.

#### 6. OOB (Out-of-Band) Managment


- iAMT (Intel Active Management)
> Hardware-based Intel® Active Management Technology provides persistent out-of-band connectivity that operates independently of the OS, allowing fixes to a wider range of systems issues, even when the OS is down. Repair corrupted drivers, application software, or the OS on non-responsive systems that will not run or boot or use KVM to monitor OS upgrades or boot to the system BIOS

The DeviceOn default integrate iAMT for OOB control, such as KVM, and power management, especially co-work with Acronis recovery solution, even your in-band system damaged, with  iAMT KVM and Acronis, it's much eaylier to do remote recovery through DeviceOn. There is unnecessary go to the field side and unbox the hardware for repairs.

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1665992566/video_to_markdown/images/youtube--6fADiZIk3zc-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/6fADiZIk3zc "")

- Advantech iBMC
> Advantech has developed a mini-Baseboard Management Controller named iBMC to provide out of band management. When the main system is abnormal or powered down, it can be powered on remotely and executed across networks, whether in public cloud or private. Second, collaborate with Apacer SSD solution, DeviceOn provides 1-click within 1s recovery even your system crashed. In some of critical scenarios, it's really helpful to reduce the operation cost, such as semi-conductor.

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1665992437/video_to_markdown/images/youtube--nptDgmCbgFY-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/nptDgmCbgFY "")


#### 7. Monitoring

With Advantech’s WISE-DeviceOn, users can swiftly utilize onboard devices, efficiently monitor device health status, such as hardware voltage, CPU, fan, hard-drive, network bandwidth sytem process, container state. 

![](https://i.imgur.com/WpwaovJ.png)


Not only that, but for Nvidia Jetson, DeviceOn build-in a Jetson dashboard for AI developer to realize the GPU status.

![](https://i.imgur.com/qpJiFGe.png)


What the benefit of using the DeviceOn?
---
Once your devices onboarding to cloud, you'll get at least benefit:

### Batch Deployment (App and Container) and Operation

The most helpful function for IT/OT operator is how to perform application, BIOS update, container deployment and scheduling control on batches of device. Through DeviceOn, we have application and container management for various scenarios, you could define and wrap your system configuration, application by yourself via online wrapper. Also, if your AI container require to rolling update, container management is your best chooise. 

### Remote Troubleshooting - Inband and OOB

Actually, in some of case, the device deployed on the tough place that's not easy to maintenance, for instance, underground or fixed on the high wall. Therefore, as possible as provide remote troubleshooting for operater will reduce lot's time, expecially DeviceOn not only inband control but out-of-band (iBMC and AMT).

### Data acquisition and Visualization

For AI developer or data scientist, the row data is the most important. WISE-Aent not just do the connectivity, remote command, but data collection from edge to cloud, even your data is audio or video, DeviceOn prodvides a mechanism for developer to retrieve these data from DeviceOn via APIs. Thinking about it another way, if there are hundred of device should collect, without DeivceOn, you must pay a lots of effort to get those device data.
