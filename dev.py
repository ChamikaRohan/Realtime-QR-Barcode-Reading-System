import cv2

def has_barcode(image):
    # Create a copy of the image to draw contours
    image_with_contours = image.copy()

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Minimum and maximum area threshold for barcode contour
    min_area = 500
    max_area = 5000

    # Iterate through contours
    for contour in contours:
        area = cv2.contourArea(contour)
        if min_area < area < max_area:
            # If a contour has area within the threshold, it might be a barcode
            cv2.drawContours(image_with_contours, [contour], 0, (0, 255, 0), 2)

            return True, image_with_contours

    # If no barcode-like contours found, return False and the original image
    return False, image


# Test with an example image
image_with_barcode = cv2.imread('Media/BarcodeImg.jpg')

# Check if images have barcode
result_with_barcode, image_with_contours = has_barcode(image_with_barcode)

# Display the result and image with contours (if barcode is found)
if result_with_barcode:
    print("Does it have QR/Barcode:", result_with_barcode)
    cv2.imshow('Image with barcode and contours', image_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Does it have QR/Barcode:", result_with_barcode)


