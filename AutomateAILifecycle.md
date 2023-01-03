# Automate AI app wrapping
To accelerate software development and maintenance, the following will demonstrates how to leveage `Azure DevOps` to create a CI/CD pipeline to push the AI container image to `Azure Container Registry`(ACR).

> [Apply an Azure account](https://www.advantech.com/zh-tw/products/19bc1aad-9be7-4664-9964-2f3893c6695f/microsoft-azure/mod_2590e2c9-e4cf-49bc-a12e-84feaa3420e9). 

## Create an ACR service
* Go to `Microsoft Azure Protal`, and then press `Create a resource`.

<p align="center">
  <img width="600" src="image\51.png">
</p>

* Type `Container Registry` and search. Select `Container Registry` in the search results and then click `Create`.

<p align="center">
  <img width="600" src="image\52.png">
</p>

<p align="center">
  <img width="600" src="image\53.png">
</p>

* Fill out the necessary info with red marks in `Basics`, and then press `Review + create` button to set an ACR resource. It may take a little time. If it succeeds, the ACR resource will show in the `Resources` list.

<p align="center">
  <img width="600" src="image\54.png">
</p>

<p align="center">
  <img width="600" src="image\55.png">
</p>

## Set up an Azure DevOps resource
### 1. Create an organization
* Go to `Microsoft Azure Protal`, and type `Azure DevOps organization` in search bar or directly click `Azure DevOps organization` if it shows in shortcut list.

<p align="center">
  <img width="600" src="image\56.png">
</p>

* Click `My Azure DevOps Organization`

<p align="center">
  <img width="600" src="image\57.png">
</p>

* If you already have `Azure DevOps Organizations`, you can jump to step 3. Or, you need to press `Create new organization` at upper right and then follow these instructions below.

<p align="center">
  <img width="600" src="image\58.png">
</p>

<p align="center">
  <img width="400" src="image\59.png">
</p>

* In this step, you can use a default organization name, enter the characters, and then press `Continue`.

<p align="center">
  <img width="400" src="image\60.png">
</p>

* While it completes, you can see the organization name listed at left.

<p align="center">
  <img width="400" src="image\61.png">
</p>

### 2. Create a project in the organization
* Press the organization and then click `New project` button. In this repo, a project, named as `Test`, was created.

<p align="center">
  <img width="600" src="image\62.png">
</p>

<p align="center">
  <img width="600" src="image\63.png">
</p>

* Click `Test` project icon and then click `Repos` to keep the repository info. Next prepare to clone this repository to the edge.

<p align="center">
  <img width="600" src="image\64.png">
</p>

<p align="center">
  <img width="600" src="image\65.png">
</p>

### 3. Commit files to  a (Azure) Repos of the project
> Make sure that you have installed [git bash](https://github.com/git-guides/install-git) on edge.
* Pull/Clone the repository from Azure Repos to the edge.

<p align="center">
  <img width="600" src="image\66.png">
</p>

* Create a directory `advan` within the cloned project `Test` on the edge and copy [required files](/advan) into `advan`.

<p align="center">
  <img width="600" src="image\68.png">
</p>

<p align="center">
  <img width="350" src="image\67.png">
</p>

* Commit `Test` on the edge to `Test` in Azure Repos.

<p align="center">
  <img width="600" src="image\69.png">
</p>

<p align="center">
  <img width="600" src="image\70.png">
</p>

* Go back to Azure DevOps|Repos, and there the committed files are also in `advan` of the `Test` project.
> Need to refresh the page if you don't see the committed files.

<p align="center">
  <img width="600" src="image\71.png">
</p>

## Build a pipelines
With the created ACR and Azure Repos, the next step is to set up a pipeline for automatically build the docker image for AI inference computing and upload the image to an ACR.  .

* Create a empty pipeline in Azure DevOps

<p align="center">
  <img width="600" src="image\72.png">
</p>

* Click `Use the classic editor`

<p align="center">
  <img width="600" src="image\73.png">
</p>

* Select `Azure Repos Git` as a source, and then press `Continue`.

<p align="center">
  <img width="600" src="image\74.png">
</p>

* Select `Docker container` as a template, and click `Apply`.

<p align="center">
  <img width="600" src="image\75.png">
</p>

* The system will preset two jobs, which correspond to our needs. All we have to do is to fill in the information.

<p align="center">
  <img width="600" src="image\76.png">
</p>

> `Name` : Key in a pipeline name
 
> `Agent pool` : Select `Azure Pipelines` in this repo

> `Agent Specification` : Select OS to be used

* Click `Get sources` and select what we used, such as `Test` mentioned in previous paragraphs, in `Team project` and `Repository`.

<p align="center">
  <img width="600" src="image\89.png">
</p>

* Click `Agent job 1` and to change `Display name` for clear understandings about what the pipeline do. And for the other two items, `Agent pool` and `Agent Specification` are the same as what were have been done when creating a `Pipeline`. (For `Agent pool`, you can also use the default `inherit from pipeline`.)

<p align="center">
  <img width="600" src="image\77.png">
</p>

* Then in the step of `Build an image`, the most important thing is `Image Name` at right bottom. You have to add the name of `Login server`, which can be found in your ACR configurtaion, to the image name. If the `Login sever` is missed, the next `Push an image` will be failed. (Here `Azure subscription` and `Azure Contianer Registry` can be skipped.)

<p align="center">
  <img width="600" src="image\78.png">
</p>

* In addtion, it's also necessary to select a `Docker File`. We can find it from the previously created directory which contains a Dockerfile, a model file and other related files for the application in this repo.

<p align="center">
  <img width="600" src="image\79.png">
</p>

* In the step of `Push an image`, fill out the items as shown ih the picture, then press `Save`, shown as the red circle.

<p align="center">
  <img width="600" src="image\82.png">
</p>

> NOTICE: 
> `Azure subscription` and `Azure Container Registry` must to be filled.
> It may need to authorize `Azure subscription`.

<p align="center">
  <img width="600" src="image\90.png">
</p>

* After you fill out all items of these two jobs, you can select `Save & queue` to save what you have done and then the pipeline will be executed after that.
* If you just want to save what you have done, you can select `Save` instead of `Save & queue`, and you can exectute this pipeline whenever you want.

<p align="center">
  <img width="600" src="image\83.png">
</p>

> For this repo, we set up `Azure Container Registry` in `Southeast Asia`.

## Monitor the CI process
* Click the Jobs you have just created and started running. You will see the process.

<p align="center">
  <img width="600" src="image\84.png">
</p>

<p align="center">
  <img width="600" src="image\85.png">
</p>

<p align="center">
  <img width="600" src="image\86.png">
</p>

<p align="center">
  <img width="600" src="image\87.png">
</p>

* Finally, if it succeeds, you can see that a new created repository has been listed in ACR for further required operations. For example, in this repo, DeviceOn will be able to further use the created repository by connecting to the ACR.

<p align="center">
  <img width="600" src="image\88.png">
</p>
