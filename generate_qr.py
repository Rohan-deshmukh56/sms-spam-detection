import qrcode

# Replace this with your public URL
url = "https://sms-spam-detection-gfmfvbak4eiomctnlxdlrq.streamlit.app/"

# Generate and save QR code
qr = qrcode.make(url)
qr.save("project_qr.png")

