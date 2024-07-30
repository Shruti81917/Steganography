
from PIL import Image
import stepic


image = Image.open("encrypted_photo.png")


decoded_msg = stepic.decode(image)

print("Decryption Completed!")

print("Decoded Message:", decoded_msg)