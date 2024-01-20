import cv2
import glob
import time
import numpy as np
from PIL import Image
from ultralytics import YOLO
from roboflow import Roboflow

# Test Basic Version2 for sign detection and warning system over images with YoloV8;
    # Opens the image and writes the warning!
    # Different approach for direct results in terminal!

# Initialize Roboflow
#rf = Roboflow(api_key="API-KEY")

# Specify project and model
#project = rf.workspace().project("traffic-sign-guy19")
#model = project.version(1).model
model = YOLO('../weights/best.pt')
# Get the DETECTED CLASSES from the result
classes = model.names

img = Image.open("../test-images/traffic-sign.jpg")

result = model.predict(source=img, conf=0.5)
# print(model)
# print(result)

# Check if signs are detected
stop_sign_index = 71  # 'Stop' sign has index 71
school_ahead_sign_index = 40  # 'School Ahead' sign has index 40

for r in result:
    # Get the detected classes from the result
    if r.boxes:
        box = r.boxes[0]
        class_id = int(box.cls)
        object_name = model.names[class_id]

        if classes[stop_sign_index] in object_name:
            #print("\nWarning: You need to stop!\n")
            text = "\nWarning: You need to stop!\n"
            im_array = r.plot()  # plot a BGR numpy array of predictions
            img_np = np.array(im_array[..., ::-1])  # Convert to NumPy array
            cv2.putText(img_np, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.imshow("Detected Image", img_np)
            cv2.waitKey(0)

        elif classes[school_ahead_sign_index] in object_name:
            print("\nWarning: There is a school ahead!\n")
        else:
            print("No school!")

        # im_array = r.plot()  # plot a BGR numpy array of predictions
        # im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        # im.show()  # show image

print("Done!")