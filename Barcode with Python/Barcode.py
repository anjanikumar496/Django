import barcode
import random
def barcode_generator():
    num = random.randrange(1,1000000000000)
    print(num)
    image = barcode.get_barcode_class('ean13')
    image_bar = image(u'{}'.format(num))
    file = open('barcode_tanya.svg',"wb")
    image_bar.write(file)
    return "Barcode Generated Successfully"
barcode_generator()
