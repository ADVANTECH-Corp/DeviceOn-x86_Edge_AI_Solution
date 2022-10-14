# DeviceOn-x86_Edge_AI_Solution
## Overview

When we talk about an overall process of Edge AI Solution, it will include data ingestion, data preprocessing, data labeling, model training and validation、model optimization, application development, application deployment and edge inference. And it's obvious that we always didn't care the time spent for the flow or pipeline integration when we carried out a POC. However there are still lots of matters necessary to be handled at that moment when we would like to transfer a POC of edge AI solution into a production stage, some things like an integrated pipeline from cloud training to edge inference, continuous deployment for AI application update, remote monitoring and management over large-scale edge AI devices and even further statistical analysis by rich inference results.

>Architecture

![image](image/project%20architecture.png)

How does Advantech act a booster of Edge AI solution?
(陳述應用痛點，並與四大產品ML service、Azure Services、DeviceOn和AI device (AIMB-288E w/ Nvidia Quadro)的特點做呼應，突顯相關產品能為客戶帶來的好處、價值)
當AI方案要從POC轉換為實際案場上可以持續運行的方案時，會有許多的因素需要被考量，甚至是許多的任務需要被處理。比方說，因為準確性調校或辨識目標變更需要經常重新訓練AI模型、安裝與更新AI應用程式的頻率次數大幅增加、遠程監管大量邊緣AI運算裝置、能夠適應惡劣環境穩定運行的邊緣AI運算裝置等等因素。為此，研華為客戶提供有Azure Custom Vision (/Edge Impulse)、Azure DevOps、Advantech DeviceOn和 Advantech AIMB-288E with NVIDIA Quadro GPU，藉由這些產品，可整合出完整的Edge AI解決方案，加速客戶的Edge AI應用導入量產與落地。

(Table)

>Use Case

![image](image/scenario.png)

Start journey with a use case of productivity monitoring for smart factory
(Background of productivity monitoring for smart factory)
接下來將透過一個客戶的實際案例，說明如何運用研華在Edge AI的相關產品，協助客戶建構一個完整的Edge AI解決方案，不僅止於POC，並且是可以持續運營的Edge AI落地應用。
客戶為了PCB產線的產能管理，希望能更即時、準確的了解發生的特定生產問題。為此，客戶希望導入視覺AI方案，提升管理效率，減少產能損失。首先，客戶歸納了產能監控的要點，一為輸送帶上是否不斷有待加工的PCB，二為工作站上的操作人員是否有正常的操作與產出。其中，關於工作站上的操作人員，由於產線畫面的視角和人員站位都有影響，為了提升視覺AI判讀人員是否在工作崗位上的準確性、可靠度，除了辨識畫面中的人形外，針對這個案例，實務上額外需要判讀人員配戴的帽子、手部、工具等。這樣的複雜辨識問題，需要相應能夠處理的AI model/AI algorithm，以及足夠算力的Edge AI device，後續我們將分享給大家，研華如何運用前面提到的幾個關鍵Edge AI產品，協助客戶一同建構出可長期運維的Edge AI應用。

## ML | Label training data
## ML | Train an accurate enough AI model
## DEV | Encapsulate a portable AI application
## DEV | Automate AI lifecycle
## OPS | Deploy AI to any edge
## OPS | Collect training, inference, and performance data
## OPS | Monitor and manage large-scale devices
## Resources and reference
