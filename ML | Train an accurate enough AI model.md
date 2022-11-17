## Train your AI model

* Click `Train` button at upper right to start training wizard after finishing data labeling.

<p align="center">
  <img width="600" src="image\7.png">
</p>

There are two types to train your model, 1)`Quick Training`; 2)`Advanced Training`. They proide difference parameters to you for setting a training procedure. Basically both of them use _training time_ to control model training instead of epochs.

### Quick Training
  * It just takes about 25 minutes no matter how many your images are adopted. The other attractive point here should be that it's free of charge so far. Therefore you can use this to do a POC for your innovatie AI applications.

<p align="center">
  <img width="600" src="image\8.png">
</p>

### Advanced Training
* Its training time takes 1 hour at least, and the maximum can be 96 hours. Certainly, here when you take more time for model training, more subscription fee will be charged.

<p align="center">
  <img width="600" src="image\9.png">
</p>

* After a training process is done, you'll see the summary of the training iteration. It includes the estimation of the model performance – Precision and Recall.

  - *Precision indicates the fraction of identified classifications that were correct.*

  - *Recall indicates the fraction of actual classifications that were correctly identified.*

  - *mAP stands for Additional Performance. This provides an additional metric, that summarizes the precision and recall at different thresholds.*

<p align="center">
  <img width="600" src="image\10.png">
</p>

* For more details, it also shows `Precision`, `Recall` and `AP` performance values of each tag in the end of the summary.

<p align="center">
  <img width="600" src="image\11.png">
</p>

> Usually `Quick Training` is applied in the beginning to train your model. Then according to performance results, you can further decide whether it is necessary to increase training time or image data, and even review current labels.
