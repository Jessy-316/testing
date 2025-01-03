from PIL import Image
import pytesseract

# Open an image file
image = Image.open('4.jpeg')

# Extract text
text = pytesseract.image_to_string(image)
print(text)
