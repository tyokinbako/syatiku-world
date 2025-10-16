from keras.models import load_model  # TensorFlow is required for Keras to work
import numpy as np
import cv2
import time
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
# Load the model
model = load_model("keras_model.h5", compile=False)
# Load the labels
class_names = open("labels.txt", "r").readlines()
# Create the array of the right shape to feed into the keras model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Initialize camera
cap = cv2.VideoCapture(0)
while True:
    # Capture frame from camera
    ret, frame = cap.read()
    if not ret:
        break
    # Resize frame to 224x224
    frame_resized = cv2.resize(frame, (224, 224))
    # Convert BGR to RGB
    frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
    # Turn the image into a numpy array
    image_array = np.asarray(frame_rgb)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    # Load the image into the array
    data[0] = normalized_image_array
    # Predict
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)
    # Display the frame
    cv2.imshow("Camera Feed", frame)
    # Wait for 0.1 second
    time.sleep(0.1)
    # Check for ‘q’ key to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# Release camera and close windows
cap.release()
cv2.destroyAllWindows()