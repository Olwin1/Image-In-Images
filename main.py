from importlib.resources import path
from PIL import Image
picture = Image.open("./images/RS.png")
original = Image.open("./images/shrek_smaller.png")

# Get the size of the image
width, height = picture.size
o_width, o_height = original.size

# Process every pixel
newcolour = (29, 230, 25)
def calcColour(a, b):
    b2 = [b[0] * 2, b[1] * 2, b[2] * 2]
    def avg(w, z):
        return round(w + z + z / 3)
    return (avg(a[0], b2[0]), avg(a[1], b2[1]), avg(a[2], b2[2]))
def createPixel(newcolour):
    for x in range(width):
        for y in range(height):
            current_color = picture.getpixel( (x,y) )
            ####################################################################
            # Change Pixel Colour
            ####################################################################
            picture.putpixel( (x,y), calcColour(current_color, newcolour))
            return picture
    #picture.show()
final = Image.new('RGB', (picture.height * original.height, picture.width * original.width))
start = [0, 0]

for x in range(int(o_width)):
    print(str(round(int(x) / original.width * 100)) + "% Complete")
    for y in range(int(o_height)):
        final.paste(createPixel(original.getpixel((x, y))), (start[0], start[1]))
        start[1] += height
    start[1] = 0
    start[0] += width
final.save("./output2.png")