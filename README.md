# DeviceOn-x86_Edge_AI_Solution
## Overview

When we talk about an overall process of Edge AI Solution, it will include data ingestion, data preprocessing, data labeling, model training and validation、model optimization, application development, application deployment and edge inference. And it's obvious that we always didn't care the time spent for the flow or pipeline integration when we carried out a POC. However there are still lots of matters necessary to be handled at that moment when we would like to transfer a POC of edge AI solution into a production stage, some things like an integrated pipeline from cloud training to edge inference, continuous deployment for AI application update, remote monitoring and management over large-scale edge AI devices and even further statistical analysis by rich inference results.

>Architecture

![image](image/project%20architecture.png)

When it comes to a production stage for edge AI solutions, the topic of continuous maintenance includes lots of extra tasks to be considered and dealt with. For example, it’s necessary to re-train an AI model owing to precision bias or target objects changed. The frequency of AI application installation and update increases to a great degree. The remote capability to manage massive and unattended edge AI devices is required. Edge AI devices are rugged enough to operate normally and continuously in terrible environments, and so on. To help deal with such problems, Advantech provides customers with Azure Custom Vision, Azure DevOps, DeviceOn and AIMB-288E with NVIDIA Quadro GPU. With the aids of these products and services, it can help construct a complete Edge AI solution and accelerate realization of solution landing or production stage migration.

| Category  | Product | Key Benefits & Features |
| ------------- | ------------- | ------------- |
| ML SaaS | Azure Custom Vision | Easily customize your own state-of-the-art computer vision models for your unique use case that no ML expertise is required |
| Dev. Pipeline | Azure DevOps | Complete or complementary services provision to automate development pipeline for packaging your AI application and cross-region development|
| Deployment & Mgmt. | **DeviceOn** | Central mgmt. platform to remotely update AI applications (OTA), and monitor and control large-scale devices at ease |
| AI Edge | (TBD)**AIMB-288E** | 12th Gen Intel® CPU integrated with NVIDIA® Quadro® GPU to fit within 1U systems while yielding 100% performance in 55 °C environments |

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
