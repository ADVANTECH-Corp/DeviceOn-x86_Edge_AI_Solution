## Training model

* Click `Train` button on upper right to start training stage.(當訓練圖片標記完成後，就可以進行訓練。點擊右上角`Train`按鈕)

<p align="center">
  <img width="600" src="image\7.png">
</p>

There are two ways to train your model, 1)`Quick Training`; 2)`Advanced Training`. It is a little bit difference from what we know about setting parameters for training. It uses _training time_ to train model instead of epochs.(根據需求選擇訓練時長，`Quick Training`大約25分鐘就訓練完成)

##### Quick Training
* It just costs about 25 minutes no matter how many your images are. The most important thing is it is free.

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
