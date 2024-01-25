#COMPUTER VISION PROJECT
#TRAFIC SIGN DETECTION AND WARNING SYSTEM
#FATMA ŞEVVAL ÇAKIROĞLU   20200203009

import cv2
import time
import numpy as np
from ultralytics import YOLO

# WARNING: real-time code ancak customize edilecek!!!

# Load the YOLOv8 model
model = YOLO('./weights/best.pt')
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
        Right_Hair_Pin_Bend_sign_index = 35
        Speed_limit_10_sign_index = 42
        Speed_limit_100_sign_index =43
        Speed_limit_110_sign_index = 44
        Speed_limit_120_sign_index = 45
        Speed_limit_130_sign_index = 46
        Speed_limit_140_sign_index =47
        Speed_limit_150_sign_index = 48
        Speed_limit_160_sign_index = 49
        Speed_limit_20_sign_index = 50
        Speed_limit_25_sign_index = 51
        Speed_limit_30_sign_index = 66
        Speed_limit_48_sign_index = 54
        Speed_limit_50_sign_index =56
        Speed_limit_55_sign_index =57
        Speed_limit_60_sign_index = 58
        Speed_limit_90_sign_index = 64
        Speed_limit_80_sign_index = 63
        Speed_limit_45_sign_index = 53
        Speed_limit_65_sign_index = 59
        Speed_limit_70_sign_index = 60
        Speed_limit_75_sign_index =61
        Slippery_Road_sign_index = 41
        Round_About_sign_index = 39
        Barrier_Ahead_sign_index = 2
        cycle_crossing_sign_index = 5
        Dangerous_Dip_sign_index = 6
        Eating_Place_sign_index = 7
        Falling_Rocks_sign_index = 8
        Ferry_sign_index = 9
        Hospital_sign_index = 13
        Left_Reverse_Bend_sign_index = 16
        Left_Hand_curve_sign_index = 17
        Light_Reflesment_sign_index = 18
        Left_Hair_Pin_Bend_sign_index = 15
        First_Aid_Post_sign_index = 10
        Give_way_sign_index = 11
        Hump_sign_index = 14
        Parking_This_Side_sign_index = 29
        Resting_Place_sign_index = 34
        Road_Wideness_Ahead_sign_index = 38
        Right_Reverse_Bend_sign_index = 37
        Right_Hand_curve_sign_index = 36
        Narrow_Road_Ahead_sign_index = 21
        No_Parking_sign_index = 22
        Narrow_Bridge_sign_index = 20

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
                    text1= "\nWarning: There is a school ahead!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text1, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_50_sign_index] in object_name:
                    text2= "\nWarning: Speed ​​Limit 50 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text2, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)                   
                elif classes[Speed_limit_100_sign_index] in object_name:
                    text3 = "\nWarning: Speed ​​Limit 100 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text3, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_110_sign_index] in object_name:
                    text4 ="\nWarning:Speed ​​Limit 110 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text4, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_120_sign_index] in object_name:
                    text5 = "\nWarning: Speed ​​Limit 120 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text5, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_130_sign_index] in object_name:
                    text6 = "\nWarning: Speed ​​Limit 130 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text6, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_140_sign_index] in object_name:
                    text7 ="\nWarning: Speed ​​Limit 140 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text7, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_150_sign_index] in object_name:
                    text8 ="\nWarning: Speed ​​Limit 150 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text8, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_160_sign_index] in object_name:
                    text9 ="\nWarning: Speed ​​Limit 160 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text9, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_60_sign_index] in object_name:
                    text10 ="\nWarning: Speed ​​Limit 60 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text10, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_90_sign_index] in object_name:
                    text11 ="\nWarning: Speed ​​Limit 90 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text11, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_80_sign_index] in object_name:
                    text12 ="\nWarning: Speed ​​Limit 80 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text12, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_20_sign_index] in object_name:
                    text13 ="\nWarning:Speed ​​Limit 20 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text13, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_25_sign_index] in object_name:
                    text14 ="\nWarning: Speed ​​Limit 25 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text14, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_30_sign_index] in object_name:
                    text15 ="\nWarning: Speed ​​Limit 30 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text15, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_45_sign_index] in object_name:
                    text16 ="\nWarning: Speed ​​Limit 45 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text16, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_48_sign_index] in object_name:
                    text17 ="\nWarning: Speed ​​Limit 48 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text17, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_55_sign_index] in object_name:
                    text18 ="\nWarning: Speed ​​Limit 55 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_65_sign_index] in object_name:
                    text19 ="\nWarning: Speed ​​Limit 65 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text19, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_70_sign_index] in object_name:
                    text20 ="\nWarning: Speed ​​Limit 70 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text20, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Speed_limit_75_sign_index] in object_name:
                    text21 ="\nWarning: Speed ​​Limit 75 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text21, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Slippery_Road_sign_index] in object_name:
                    text22 ="\nWarning: Slippery Road!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text22, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Round_About_sign_index] in object_name:
                    text23 ="\nWarning: Round About!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text23, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Barrier_Ahead_sign_index] in object_name:
                    text24 ="\nWarning: Barrier Ahead!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text24, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[cycle_crossing_sign_index] in object_name:
                    text25 ="\nWarning: cycle crossing!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text25, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Dangerous_Dip_sign_index] in object_name:
                    text26 ="\nWarning: Dangerous Dip!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text26, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Eating_Place_sign_index] in object_name:
                    text27 ="\nWarning: Eating Place!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text27, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Falling_Rocks_sign_index] in object_name:
                    text28 ="\nWarning: Falling Rocks!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text28, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Ferry_sign_index] in object_name:
                    text29 ="\nWarning: Ferry!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text29, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Hospital_sign_index] in object_name:
                    text30 ="\nWarning: Hospital!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text30, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Left_Reverse_Bend_sign_index] in object_name:
                    text31 ="\nWarning: Left Reverse Bend!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text31, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Left_Hand_curve_sign_index] in object_name:
                    text32 ="\nWarning: Left Hand curve!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text32, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Light_Reflesment_sign_index] in object_name:
                    text33 ="\nWarning: Light Reflesment!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text33, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Left_Hair_Pin_Bend_sign_index] in object_name:
                    text34 ="\nWarning: Left Hair Pin Bend!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text34, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[First_Aid_Post_sign_index] in object_name:
                    text35 ="\nWarning: First Aid Post!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text35, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Give_way_sign_index] in object_name:
                    text36 ="\nWarning: Give way!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text36, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Hump_sign_index] in object_name:
                    text37 ="\nWarning: Hump!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text37, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Parking_This_Side_sign_index] in object_name:
                    text38 ="\nWarning:Parking This Side!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text38, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Resting_Place_sign_index] in object_name:
                    text39 ="\nWarning: Resting Place!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text39, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Road_Wideness_Ahead_sign_index] in object_name:
                    text40 ="\nWarning: Road Wideness Ahead!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text40, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Right_Reverse_Bend_sign_index] in object_name:
                    text41 ="\nWarning: Right Reverse Bend!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text41, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Right_Hand_curve_sign_index] in object_name:
                    text42 ="\nWarning: Right Hand curve!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text42, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Right_Hair_Pin_Bend_sign_index] in object_name:
                    text43 ="\nWarning: Right Hair Pin Bend!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text43, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[Narrow_Road_Ahead_sign_index] in object_name:
                    text44 ="\nWarning: Narrow Road Ahead!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text44, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                elif classes[No_Parking_sign_index] in object_name:
                    text45 ="\nWarning: No Parking!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text45, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2) 
                elif classes[Narrow_Bridge_sign_index] in object_name:
                    text46 ="\nWarning: Narrow Bridge!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text46, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  
                else:
                    print("No Detection!")

            # Display the annotated frame
            cv2.imshow("YoloV8 Detection - Traffic Signs", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()