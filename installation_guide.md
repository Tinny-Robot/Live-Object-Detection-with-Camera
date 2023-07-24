# Installation Guide

Follow the steps below to set up your environment and install the required dependencies for the "Live Object Detection with YOLO and OpenCV" project.

## Prerequisites

- Python 3.6 or higher is required to run the code.
- Ensure you have a webcam or any camera connected to your computer for live video feed.

## Step 1: Clone the Repository

Clone the project repository from GitHub to your local machine using the following command:

```
git clone https://github.com/your_username/live-object-detection.git
```

## Step 2: Navigate to the Project Directory

Navigate to the directory where the repository is cloned:

```
cd live-object-detection
```

## Step 3: Install Dependencies

The project relies on several Python libraries. You can install them using `pip` or `conda`. We recommend using a virtual environment to manage the dependencies. Here's how:

1. Create a virtual environment (optional) and activate it:

   ```
   # Using virtualenv (optional)
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required dependencies from the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

This will install the necessary libraries, including OpenCV, supervision, and ultralytics, which are required for running the live object detection demo.

## Step 4: Download YOLO Model Weights

The YOLO model weights are not included in the repository due to their large size. You can download the pre-trained model weights (e.g., "yolov8n.pt") from the official YOLO website or other reputable sources. Place the downloaded model weights in the project directory.

## Step 5: Run the Live Object Detection Demo

You are now ready to run the live object detection script. Open the Jupyter notebook "demo.ipynb" in your Jupyter environment. Run each cell in the notebook to execute the live object detection demo. Make sure your webcam or camera is accessible and properly connected.

## Next Steps

After successfully setting up the environment and running the live object detection demo, you can proceed to customize the project based on your specific needs. Refer to the "Customization Guide" for instructions on how to adjust the confidence threshold, modify bounding box annotations, and select specific object classes for detection.

Enjoy exploring the world of real-time object detection with YOLO and OpenCV! If you have any questions or need assistance, feel free to reach out or check the repository's `README` for more information.
