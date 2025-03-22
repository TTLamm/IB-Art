import qrcode

# Define the URL or file path to your image
image_url = "https://your-image-link.com/image.jpg"

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
qr_image = qr.make_image(fill="black", back_color="white")

# Save the QR code image
qr_image.save("qr_code.png")

print("QR code generated and saved as 'qr_code.png'")
