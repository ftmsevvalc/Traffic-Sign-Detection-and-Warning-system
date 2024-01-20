<div align="center">
<img src="https://cdn-icons-png.flaticon.com/512/8708/8708013.png" width="200" height="200" alt="traffic-signs">
</div>

<h1 align="center">Traffic Sign Detection & Warning System - YOLOv8</h1>

*  [:hash: Purpose](#hash-purpose)
*  [:hash: How To Run or Develop?](#hash-how-to-run-or-develop)

<p align="justify">

# :hash: Purpose
This project is developed with the aim of detecting traffic signs using the YOLOv8 object detection model and displaying appropriate warnings to drivers in real time. This repo also contains test files that YOLOv8 object detection through images and different aspects of loading custom dataset model.

**Dataset Preparation** <br>
The dataset used in this project has been obtained through the Roboflow platform. Roboflow is a tool used to create and manage labeled image datasets with also used as open source. [Visit Custom Dataset Model!](https://universe.roboflow.com/fsevval/traffic-sign-guy19)

**Model Training** <br>
Google Colab and the YOLOv8 notebook were used for model training. To follow the training steps, see the _How to run or develop this type of project?_

# :hash: How To Run or Develop?
**Model Training** <br>
1. Create a new notebook in Google Colab.
2. Install the necessary dependencies within the YOLOv8 notebook.
3. Upload your dataset to Google Drive and access it through the notebook.
4. Train the model by following the notebook step by step.
5. Save the obtained weights file with the .pt extension at the end of training.

**Code Usage** <br>
1. Add the .pt weight file obtained at the end of training to the weights folder.
2. Run the traffic sign detection and warning system application using the test-real.py file.
```
git clone https://github.com/ftmsevvalc/Traffic-Sign-Detection-and-Warning-system.git
```
```
cd Traffic-Sign-Detection-and-Warning-system
```
```
python3 real-time.py
```
</p>