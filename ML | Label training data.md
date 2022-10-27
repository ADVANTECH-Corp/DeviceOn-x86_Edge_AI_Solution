### 登入Azure的Custom Vision - Home

<p align="center">
  <img width="600" src="image\1.png">
</p>

### 建立新專案

* 填寫必填欄位內容
* 若沒有`Resource`可以直接點選`create new`新增，若已建立好，則可以選擇既有的

* 本例以物件偵測為主，所以在`Project Types`上選擇`Object Detection`

* 若有離線推論的需求，需在`Domains`上選擇`General (compacr) [S1]`

<p align="center">
  <img width="600" src="image\2.png">
</p>

### 新增圖片

* 按下`Add images`後，選取欲訓練且未標記的資料
* 上傳完成後，左側的`Untagged`會提醒有未標記的圖片

<p align="center">
  <img width="600" src="image\3.png">
</p>

> 未必要把所有未標記的圖片標記完後才能進行模型的訓練，但是訓練資料量不足時是無法進行訓練的

### 標記圖片

* 點選`Untagged`，便可以對裡面的照片進行標記

<p align="center">
  <img width="600" src="image\4.png">
</p>

<p align="center">
  <img width="600" src="image\5.png">
</p>

* 標記完後，畫面左下角會顯示各標記類別的數量

<p align="center">
  <img width="600" src="image\6.png">
</p>
