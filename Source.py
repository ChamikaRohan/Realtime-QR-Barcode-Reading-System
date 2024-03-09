import cv2

from pyzbar.pyzbar import decode

def detect_barcode(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect and decode barcodes and QR codes
    barcodes = decode(gray)

    for barcode in barcodes:
        # Extract the bounding box location of the barcode
        (x, y, w, h) = barcode.rect

        # Draw a rectangle around the barcode
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Get the data contained in the barcode
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Display the barcode data and type
        text = "{} ({})".format(barcode_data, barcode_type)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Print the barcode data and type to the console
        print("Found {} barcode: {}".format(barcode_type, barcode_data))

    return frame

def main():
    # Open default camera (usually the webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Detect barcode in the frame
        frame_with_barcode = detect_barcode(frame)

        # Display the frame with detected barcode in real-time
        cv2.imshow('Barcode Detection', frame_with_barcode)

        # Press 'q' to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
