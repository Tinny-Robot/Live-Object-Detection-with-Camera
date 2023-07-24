import cv2
import supervision as sv
from ultralytics import YOLO

def live_object_detection():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    model = YOLO("yolov8n.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    while True:
        ret, frame = cap.read()

        data = model(frame)
        detection = sv.Detections.from_yolov8(data[0])

        label = [f"{model.model.names[ci]} {con:0.2f}"
                 for _, _, con, ci, _ in detection]

        if not ret:
            print("Error: Failed to grab frame.")
            break

        frame = box_annotator.annotate(scene=frame, detections=detection, labels=label)

        # Display the live camera feed with object detection annotations
        cv2.imshow("Live Object Detection", frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

# Run the live object detection function
live_object_detection()
