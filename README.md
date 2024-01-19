YOLOv8 Traffic Sign Detection and Warning System
This project is developed with the aim of detecting traffic signs using the YOLOv8 object detection model and displaying appropriate warnings to drivers.

Dataset Preparation
The dataset used in this project has been obtained through the Roboflow platform. Roboflow is a tool used to create and manage labeled image datasets.

Create a new project in your Roboflow account.
Upload and label your images.
Obtain the YOLOv8 compatible dataset as output from Roboflow.
Model Training
Google Colab and the YOLOv8 notebook were used for model training. To follow the training steps, you can:

Create a new notebook in Google Colab.
Install the necessary dependencies within the YOLOv8 notebook.
Upload your dataset to Google Drive and access it through the notebook.
Train the model by following the notebook step by step.
Save the obtained weights file with the .pt extension at the end of training.
Code Usage
To run the project code, follow these steps:

Add the .pt weight file obtained at the end of training to the weights folder.
Run the traffic sign detection and warning system application using the test-real.py file.
bash
Copy code
python test-real.py
These steps cover the usage of the YOLOv8 model for traffic sign detection and the implementation of the warning system. You can use this README file and the codes to organize and customize your project files.
