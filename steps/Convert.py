
import base64
import io
from PIL import Image

class ImageEncoder:

    def base64_encode_image(self, image):
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG") # type: ignore
        img_str = base64.b64encode(buffered.getvalue())
        return img_str.decode("utf-8")

    def base64_decode_image(self, encoded_img):
        img_bytes = encoded_img.encode("utf-8") 
        img_buffer = io.BytesIO(base64.b64decode(img_bytes))
        return Image.open(img_buffer)

# # Usage
# encoder = ImageEncoder()
#
# # Encode
# with open("image.jpg", "rb") as img_file:
#     img = Image.open(img_file)
#     encoded_img = encoder.base64_encode_image(img)
#     print(encoded_img)
#
# # Decode
# decoded_img = encoder.base64_decode_image(encoded_img)
# decoded_img.show() # View image