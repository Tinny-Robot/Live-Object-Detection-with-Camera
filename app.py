from ultralytics import YOLO
import cv2

# Load the YOLO model (YOLOv8 in this case)
model = YOLO('yolov8n.pt') 

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Make prediction
    results = model(frame)
    
    # results is a list, so we need to iterate through it
    for result in results:
        # Visualize results
        annotated_frame = result.plot()
    
        # Display the frame
        cv2.imshow("Real-time Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
