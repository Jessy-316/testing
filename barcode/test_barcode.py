# test_barcode.py
import barcode
from barcode.writer import ImageWriter

# Create a barcode
code = barcode.get('ean13', '123456789012', writer=ImageWriter())
code.save('my_barcode')

print("Barcode saved as 'my_barcode.png'")
