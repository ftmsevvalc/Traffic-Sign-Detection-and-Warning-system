import cv2
import time
import numpy as np
from ultralytics import YOLO

# Template of real-time sign detection and warning system!

# Load the YOLOv8 model
model = YOLO('../weights/best.pt')
classes = model.names

cap = cv2.VideoCapture(0)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        result = model.predict(frame, conf=0.6)

        # Visualize the results on the frame
        annotated_frame = result[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Testing", annotated_frame)
        
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
                    text = "\nWarning: You need to stop!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

                elif classes[school_ahead_sign_index] in object_name:
                    print("\nWarning: There is a school ahead!\n")
                else:
                    print("No school!")

            # Display the annotated frame
            cv2.imshow("YoloV8 Detection - Traffic Signs", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()