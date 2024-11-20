import cv2

def capture_image(output_filename="captured_image.jpg"):
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # 0 is the default camera; change if using a different camera

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return

    print("Camera is ready. Press 'c' to capture an image or 'q' to quit.")
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Display the live video feed
        cv2.imshow('Live Feed', frame)

        # Wait for user input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):  # Press 'c' to capture
            cv2.imwrite(output_filename, frame)
            print(f"Image captured and saved as {output_filename}")
            break
        elif key == ord('q'):  # Press 'q' to quit without capturing
            print("Exiting without capturing an image.")
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()
