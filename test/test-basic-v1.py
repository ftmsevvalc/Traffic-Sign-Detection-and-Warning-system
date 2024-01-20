import glob
from roboflow import Roboflow

# Test Basic Version1 for sign detection and warning system over images with YoloV8;
    # No image opens, just writes the warning in terminal!
    # An approach for direct results in terminal!

# Initialize Roboflow
rf = Roboflow(api_key="API_KEY")

# Specify project and model
project = rf.workspace().project("traffic-sign-guy19")
model = project.version(1).model

# Perform prediction on all images in the folder
#image_paths = glob.glob("test/*.jpg")
# Iterate for each image in the folder
# for image_path in image_paths:
#     result = print(model.predict(image_path, confidence=40, overlap=30).json())

# Perform prediction on a specific image
result = model.predict("../test-images/traffic-sign2.jpg", confidence=40, overlap=30)

# Check if signs are detected
if 'predictions' in result.json():
    for prediction in result.json()['predictions']:
        if prediction['class'] == 'Stop':
            print("\nWarning: You need to stop!\n")

        if prediction['class'] == 'School Ahead':
            print("\nWarning: There is a school!\n")
        else:
            print("No school!")

# Print the full prediction result (optional)
print(result.json())