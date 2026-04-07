from PIL import Image
from PIL.ExifTags import TAGS
import io

def extract_exif(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        exif_data_raw = image._getexif()

        if not exif_data_raw:
            return {"error": "No EXIF data"}

        exif_data = {}

        for tag, value in exif_data_raw.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value

        return exif_data

    except Exception as e:
        return {"error": str(e)}
