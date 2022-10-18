# Operation - Collect Training, Inference, and Performance Data

Purpose
---
The data scientists typically would like to understand two results as deploying AI inference to the edge device. First, how the accuracy of inference? Second, how could it continue to upload the raw data to a training platform automatically for next time training?

In the section, tried to describe and guide you how the DeviceOn to assist data scientists to do data acquisition on the edge device and report the inference result to the server.

Prerequisites
---

- A workable DeviceOn server must be installed and running without problems. You could refer to the [documentation](https://docs.wise-paas.advantech.com/en/Guides_and_API_References/ApplicationServices/1564727799415968385/1589506780729736622/v1.0.0) of DeviceOn to set up your own server.
- An edge device must be installed WISE-Agnet and onboarding to DeviceOn server. You may refere to [Operation - Deploy AI to Edge Device](/OPS%20%7C%20Deploy%20AI%20to%20any%20edge.md) for details.

Step 1: How to Upload Your Training Data and Automatically
---

 ### <font color=darkgrey>1. Upload to Third-Party Storage (T.B.C)</font>
 
 ### <font color=darkgrey>2. Upload to Azure Custom Vision (T.B.C)</font>


Step 2: How to Upload Your Inference Data
---
### 1. Through Key-Value Plugin of WISE-Agent
Assuming your inference result is numeric, boolean, for example model's accuracy (%), the age of the person or gender. Those types could adopt the Key-Value mechanism to upload to the DeviceOn server. 

 #### <font color=darkred>***Key-Value Characteristics:***</font>
>Developers do not need to spend lot’s time to understand the WISE-Agent core, handshake protocol, and focus on obtaining their sensor data and using the development language they are familiar with. 

![](https://i.imgur.com/JJsZqye.png)


* One code or mechanism for all platform (Windows/Linux/RISC)
* Any development language that you are familiar with.

 #### Where can I get the ***kvClient.exe***?
You could get the kvclient tool in the WISE-Agent installer folder, for example:
```bash
<WISEAgent Install Folder>\tools\kvclient
```
 #### <table><tr><td bgcolor=#F0F0F0><font color=#0066CC>**Data Upload**</font></td></tr></table>
 
We provide 3 input formats to describe these parametes:
 #### **Argument**
This is a command line input format. You can just append "PLUGIN_NAME", "Key" and "value" as the argument, each argument must separator by **blank**:
```bash
kvclient <PLUGIN_NAME> <key1=value1> <key2=value2>
```
<table><tr><td bgcolor=#F0F0F0><font color=Green><strong>Example: </strong></font></td></tr></table>

```bash
kvclient report MyPlugin "Sensor1=Value1" "Sensor2=Value2"
```

 #### **One String**
This is the similar with argument input format, except the separator is changed to **triple underline**, "**___**". For example:
```bash
kvclient "___<PLUGIN_NAME>___key1=value1___key2=value2"
```
<table><tr><td bgcolor=#F0F0F0><font color=Green><strong>Example: </strong></font></td></tr></table>

```bash
kvclient report "___MyPlugin___Sensor1=Value1___Sensor2=Value2"
```

 #### **File**
Argument has length limit in different operating system, hence kvlcient provide a file input format that read sensor data from specified file. The command format would like to
```bash
kvclient -f <File_Name>
```

<table><tr><td bgcolor=#F0F0F0><font color=Green><strong>Example: </strong></font></td></tr></table>

```bash
kvclient report -f report.txt
```

<table><tr><td bgcolor=#F0F0F0><font color=Green><strong>File Example: </strong></font></td></tr></table>

```bash
MyPlugin
Sensor1=value1
Sensor2=value2
```

No matter which input format you choose, in the end, there is a new plugin called **MyPlugin** on the DeviceOn portal.

![](https://i.imgur.com/gIxkjXd.png)

![](https://i.imgur.com/iQCW8hI.png)

 #### <table><tr><td bgcolor=#F0F0F0><font color=#0066CC>**Advanced**</font></td></tr></table>

>Sensor Value Type: 
There are 3 value types that defined in DeviceOn, **String**, **Numeric** and **Boolean**. We give a symbol for each type.
>> s, String
> n, Numberic (int, double)
> b, Boolean

Therefore, you can specific the type of each sensor value by adding prefixed symbol before value. For examples: 

- Report a **String** type for sensor1 value to "123":
```
kvclient report MyPlugin "Sensor1=123"
```

- Report a **Numberic** type for sensor1 value to "123":
```
kvclient report MyPlugin "Sensor1=n,123"
```

- Report a **Boolean** type for sensor1, value to "true":
```
Kvclient report MyPlugin "Sensor1=b,true"
```

<table><tr><td bgcolor=#F0F0F0><font color=Green><strong>Response</strong></font></td></tr></table>

The response message is separator by triple underline "**___**", and the format is following:
   1. response: function prefix.
   2. seq: The unique sequence id of this message.
   3. result: Result code ID, where 0 is success, others is error.
   4. msg: Readable error message.

> **Success**:
```bash
kvclient report MyPlugin "Sensor1=Value1" "Sensor2=Value2"
response___seq=1___result=0
```

> **Failed**: 
```bash
kvclient report MyPlugin
response___seq=-1___result=-1___msg=invalid input
```

<table><tr><td bgcolor=#F0F0F0><font color=Green><strong>Debug</strong></font></td></tr></table>
To debug your command and message, try to add an option parameter to print sensor data.

- **-v**: Verbose, print debug message and sensor informaion.
![](https://i.imgur.com/x89zAV8.png)

- **-d**: Dry run, doesn’t send any message to server, just print debug message and sensor information.
![](https://i.imgur.com/VLdvFp9.png)



<table><tr><td bgcolor=#F0F0F0><font color=Green><strong>Keepalive Mode (Websocket)</strong></font></td></tr></table>

kvclient support keepalive mode (websocket), it can reduce the protocol overhead and continue to read user input for sending data and event log. You can add keepalive option (-k) to enter keepalive mode.

```bash
Kvclient report -v -k
```
![](https://i.imgur.com/8zcfOcV.png)
Then you can continue to enter sensor data input. 

<table><tr><td bgcolor=#FFD9D9><font color=black>Only support "One String" input format in keepalive mode.</font></td></tr></table>

![](https://i.imgur.com/y3tXiBh.png)


Enter "**exit**" or **Ctrl+C** to terminate keepalive mode.

<table><tr><td bgcolor=#F0F0F0><font color=Green><strong>Configuration</strong></font></td></tr></table>

The KeyValue pluign default adopt port **3799** for **HTTP/WebSocket** service, you could adjust the configuration file, **kvhandler.ini**, if requried.

```bash
<WISEAgent Install Forder>\kvhandler.ini
```

You can unmark parameter by remove "**#**" symbol in INI file. 
- port: Key-Value plugin will listen on port **3799**, you could change the listen port. Base on this change, kvclient tool should change the default connection port by port option (**-p**)
- cache: Key-Value plugin will not cache your sensor data in default, the cache data used to data difference report.

```bash=
[kvserver]
#port=3799
#cache=0
``` 
 
### <font color=darkgrey>2. Through DeviceOn Data Synchronize (T.B.C)</font>
 

What the benefit of using the Plugin of WISE-Agent?
---
