# Customization Guide

The "Live Object Detection with YOLO and OpenCV" project provides various customization options that allow you to tailor the real-time object detection system to your requirements. This guide will walk you through the available customization options and how to modify the code to achieve your desired changes.

## Adjust Confidence Threshold

The confidence threshold controls the sensitivity of the object detection system. Lowering the threshold may result in more detections with lower confidence scores, while increasing it will only display high-confidence detections. To adjust the confidence threshold:

1. Open the `live.py` Python file in your preferred code editor.
2. Locate the following line of code:

   ```python
   # Set the confidence threshold (0.3 by default)
   confidence_threshold = 0.3
    ```
3. Change the value of `confidence_threshold` to your desired confidence score (between 0 and 1).
4. Save the file and run the script again to see the effects of the new threshold.

## Modify Bounding Box Annotations

You can customize the appearance of bounding box annotations for detected objects. To modify the box annotations:

1. Open the `live.py` Python file in your preferred code editor.
2. Locate the box annotator setup section:

   ```python
   # Initialize the box annotator for visualizing detections
   box_annotator = sv.BoxAnnotator(
       thickness=2,
       text_thickness=2,
       text_scale=1
   )
   ```

3. You can change the values of `thickness`, `text_thickness`, and `text_scale` to adjust the appearance of the bounding boxes and text labels.
4. Save the file and run the script again to see the updated bounding box annotations.

## Select Specific Object Classes

If you are interested in detecting only specific object classes or excluding some classes, you can do so by modifying the list of selected classes.

1. Open the `live.py` Python file in your preferred code editor.
2. Find the following line of code:

   ```python
   # Extract labels and confidence scores for the detected objects
   label = [f"{model.model.names[ci]} {con:0.2f}"
            for _, _, con, ci, _ in detection]
   ```

3. By default, this code includes all the detected classes. You can customize the `label` list comprehension to include only the classes you want to display. For example, to detect only "person" and "car," you can modify the code as follows:

   ```python
   label = [f"{model.model.names[ci]} {con:0.2f}"
            for _, _, con, ci, _ in detection if model.model.names[ci] in ["person", "car"]]
   ```

4. Save the file and run the script again to see the changes with the selected classes.

Feel free to experiment with these customization options to tailor the "Live Object Detection with YOLO and OpenCV" project to suit your specific use cases and preferences. If you encounter any issues or have further questions, refer to the "Troubleshooting Guide" or feel free to ask for assistance in the repository's issues section.

Happy customizing!