## Train your AI model

* Click `Train` button at upper right to start training wizard after finishing data labeling.

<p align="center">
  <img width="600" src="image\7.png">
</p>

There are two ways to train your model, 1)`Quick Training`; 2)`Advanced Training`. They proide difference parameters to you for setting a training procedure. Basically both of them use _training time_ to control model training instead of epochs.

##### Quick Training
* It just takes about 25 minutes no matter how many your images are adopted. The other attractive point here should be that it's free of charge so far. Therefore you can use this to do a POC for your innovatie AI applications.

<p align="center">
  <img width="600" src="image\8.png">
</p>

##### Advanced Training
* The minimum training time is 1 hour, and the longest one is 96 hours. But, the more time you spend, the more money it charges. 則是1小時為單位，最長可以訓練96小時(收費機制會隨訓練時間的增長而增加)

<p align="center">
  <img width="600" src="image\9.png">
</p>

* After training, the results, which are `Precision`, `Recall` and `mAP`, will be shown on the screen.(訓練完成後會顯示模型的`Precision`、`Recall`以及`mAP`的數值)

<p align="center">
  <img width="600" src="image\10.png">
</p>

* It also shows `Precision`, `Recall` and `AP` of each tags, which are below the model results.(下方則顯示各類別的`Precision`、`Recall`以及`AP`的數值)

<p align="center">
  <img width="600" src="image\11.png">
</p>

> It may be efficient to apply `Quick Training` first to train your model, and then according to the results, decide whether it is necessary to increase the training time or image data. (可以先使用`Quick Training`進行訓練，再根據結果來決定是否增加訓練時間)
