import cloudinary
from cloudinary.uploader import upload

# Configuration
cloudinary.config(
    cloud_name = "dtcpcdhky",
    api_key = "873597142911557",
    api_secret = "GvkrY6yumXk6ayEEPuh3nbVWQUM", # Click 'View API Keys' above to copy your API secret
    secure=True
)

def uploadImage(img):
    # Upload an image
    upload_result = upload(img)
    return upload_result["secure_url"]