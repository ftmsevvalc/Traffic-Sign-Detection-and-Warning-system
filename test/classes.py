# YOLOV8 Custom Trained Model Class Names (classes)
# Roboflow and Google Colab used
    # Stored as file in case of needed...
names: {
    0: '-', 
    1: '0', 
    2: 'Barrier Ahead', 
    3: 'Cattle', 
    4: 'Caution', 
    5: 'Cycle Crossing', 
    6: 'Dangerous Dip', 
    7: 'Eating Place', 
    8: 'Falling Rocks', 
    9: 'Ferry', 
    10: 'First Aid Post', 
    11: 'Give Way', 
    12: 'Horn Prohibited', 
    13: 'Hospital', 
    14: 'Hump', 
    15: 'Left Hair Pin Bend', 
    16: 'Left Reverse Bend', 
    17: 'Left hand curve', 
    18: 'Light Refreshment', 
    19: 'Men at Work', 
    20: 'Narrow Bridge', 
    21: 'Narrow road ahead', 
    22: 'No Parking', 
    23: 'No Stopping', 
    24: 'No Thorough Road', 
    25: 'No Thorough SideRoad', 
    26: 'Parking Lot Cars', 
    27: 'Parking Lot Cycle', 
    28: 'Parking Lot Scooter and MotorCycle', 
    29: 'Parking This side', 
    30: 'Pedestrian Crossing', 
    31: 'Pedestrian Prohibited', 
    32: 'Petrol Pump- Gas Station',
    33: 'Public Telephone', 
    34: 'Resting Place', 
    35: 'Right Hair Pin Bend', 
    36: 'Right Hand Curve', 
    37: 'Right Reverse Bend', 
    38: 'Road Wideness Ahead', 
    39: 'Round About', 
    40: 'School Ahead', 
    41: 'Slippery Road', 
    42: 'Speed Limit -10-', 
    43: 'Speed Limit -100-', 
    44: 'Speed Limit -110-', 
    45: 'Speed Limit -120-', 
    46: 'Speed Limit -130-', 
    47: 'Speed Limit -140-', 
    48: 'Speed Limit -150-', 
    49: 'Speed Limit -160-', 
    50: 'Speed Limit -20-', 
    51: 'Speed Limit -25-', 
    52: 'Speed Limit -35-', 
    53: 'Speed Limit -45-', 
    54: 'Speed Limit -48-', 
    55: 'Speed Limit -5-', 
    56: 'Speed Limit -50-', 
    57: 'Speed Limit -55-', 
    58: 'Speed Limit -60-', 
    59: 'Speed Limit -65-', 
    60: 'Speed Limit -70-', 
    61: 'Speed Limit -75-', 
    62: 'Speed Limit -8-', 
    63: 'Speed Limit -80-', 
    64: 'Speed Limit -90-', 
    65: 'Speed Limit 3', 
    66: 'Speed Limit 30', 
    67: 'Speed limit -15-', 
    68: 'Speed limit -40-', 
    69: 'Steep Ascent', 
    70: 'Steep Desecnt', 
    71: 'Stop', 
    72: 'Straight Prohibitor No Entry', 
    73: 'walking'
}
# See valid attributes of custom trained model below in case of needed...
#     A class for storing and manipulating inference results.
#     Args:
#         orig_img (numpy.ndarray): The original image as a numpy array.
#         path (str): The path to the image file.
#         names (dict): A dictionary of class names.
#         boxes (torch.tensor, optional): A 2D tensor of bounding box coordinates for each detection.
#         masks (torch.tensor, optional): A 3D tensor of detection masks, where each mask is a binary image.
#         probs (torch.tensor, optional): A 1D tensor of probabilities of each class for classification task.
#         keypoints (List[List[float]], optional): A list of detected keypoints for each object.

#     Attributes:
#         orig_img (numpy.ndarray): The original image as a numpy array.
#         orig_shape (tuple): The original image shape in (height, width) format.
#         boxes (Boxes, optional): A Boxes object containing the detection bounding boxes.
#         masks (Masks, optional): A Masks object containing the detection masks.
#         probs (Probs, optional): A Probs object containing probabilities of each class for classification task.
#         keypoints (Keypoints, optional): A Keypoints object containing detected keypoints for each object.
#         speed (dict): A dictionary of preprocess, inference, and postprocess speeds in milliseconds per image.
#         names (dict): A dictionary of class names.
#         path (str): The path to the image file.
#         _keys (tuple): A tuple of attribute names for non-empty attributes.