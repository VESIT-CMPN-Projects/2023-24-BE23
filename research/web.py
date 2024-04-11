import streamlit as st
from PIL import Image
from ultralytics import YOLO
import os
st.title("YOLOv8 fish Detection")

# Load YOLO model
def load_model():
    return YOLO('./best.pt')

model = load_model()

# Function to perform object detection
def detect_objects(image):
    predictions = model.predict(image, show=True, save=True)
    return predictions

# Upload image
image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if image_file is not None:
    # Display uploaded image
    image = Image.open(image_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Perform object detection when button is clicked
    #if st.button("Detect Fish"):
    with st.spinner("Detecting fishes..."):
        # Perform object detection
        input_path = os.path.join('data', image_file.name)
        predictions = model.predict(input_path, show=True, save=True)

        # Get the directory containing the prediction results
        save_dir = predictions[0].save_dir

        # Get the name of the original image file
        image_name = os.path.basename(image_file.name)
        print(image_name)

        # Form the path to the prediction result image
        prediction_result_path = os.path.join(save_dir, image_name)
        print(prediction_result_path)

        # Display the prediction result image
        if os.path.exists(prediction_result_path):
            predicted_image = Image.open(prediction_result_path)
            st.image(predicted_image, caption="Prediction Results", use_column_width=True)
        else:
            st.error("Prediction results not found!")

