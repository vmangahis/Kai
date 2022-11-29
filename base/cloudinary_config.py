from decouple import config
import cloudinary
import cloudinary.uploader



def runConfig():
    cloudinary.config( 
        cloud_name = config("CLOUDINARY_NAME"), 
        api_key = config("CLOUDINARY_API_KEY"), 
        api_secret = config("CLOUDINARY_SECRET_API") 
    )
    #cloudinary.uploader.upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg", public_id = "olympic_flag")