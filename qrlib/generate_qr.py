import qrcode

def generate_qr_code(uuid_str):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,  # Controls size (1 is the smallest, 40 is the largest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border thickness
    )
    
    url = f"https://www.x.com/qr?uuid={uuid_str}" # Temporary URL

    # Add UUID to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create and save the QR code as an image
    img = qr.make_image(fill="black", back_color="white")
    return img