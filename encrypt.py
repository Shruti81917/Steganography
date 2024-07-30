

from PIL import Image
import stepic


img = Image.open("photo.jpg")

message = "Hey there! Welcome to CodeSpeedy."

message = message.encode()

encoded_img = stepic.encode(img, message)

encoded_img.save("encrypted_photo.png")

print("Encryption Completed!")