import qrcode
import cv2
import numpy as np

# Define the URL or file path to your image
image_url = "https://github.com/TTLamm/IB-Art/blob/main/IB%20Art%20Class%202015.jpg?raw=true"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 = small, higher = larger)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for readability
    box_size=10,  # Size of each QR box
    border=4,  # Border thickness
)

# Add data to the QR code
qr.add_data(image_url)
qr.make(fit=True)

# Generate an image from the QR Code
qr_image = qr.make_image(fill_color="darkred", back_color="white")

# Save the QR code image
qr_image.save("qr_code_colored.png")

# Load QR code
qr_code = cv2.imread("qr_code_colored.png", cv2.IMREAD_UNCHANGED)

# Load Spartan Helmet Mask (Make sure it's a transparent PNG)
mask = cv2.imread("spartan_helmet.png", cv2.IMREAD_UNCHANGED)
mask = cv2.resize(mask, (qr_code.shape[1], qr_code.shape[0]))  # Resize to match QR

# Convert mask to binary
gray_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
_, binary_mask = cv2.threshold(gray_mask, 100, 255, cv2.THRESH_BINARY)

# Apply mask to QR code
spartan_qr = cv2.bitwise_and(qr_code, qr_code, mask=binary_mask)

# Save final QR Code
cv2.imwrite("spartan_qr.png", spartan_qr)

print("QR Code in Spartan shape generated!")
