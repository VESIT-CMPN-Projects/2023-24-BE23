# YOLOv8 Object Detection Streamlit App

This repository contains a Streamlit app for fish detection using the YOLOv8 model. The app allows users to upload images and perform object detection on them.

## Dataset link

fishnet.ai v0.1.2

## Instructions

To run the app locally, follow these steps:

### 1. Clone the Repository

### 2. Set Up a Virtual Environment (optional but recommended)

```sh
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Install Dependencies

The `requirements.txt` file contains the necessary packages:

```sh
pip install -r requirements.txt
```

### 4. Run the Streamlit App

streamlit run app.py

```sh
streamlit run app.py
```

The app should now be running locally on your machine. You can access it by opening a web browser and navigating to [http://localhost:8501](http://localhost:8501).

## Sample Input Data

Sample input data for testing the app can be found in the `data` folder.

## YOLO Weights

The YOLOv8 weights file (`best.pt`) should be placed in the root directory of the repository.
