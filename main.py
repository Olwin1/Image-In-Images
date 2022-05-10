from PIL import Image
import numpy as np
picture = Image.open("./images/***REMOVED***")
original = Image.open("./images/***REMOVED***")

# Get the size of the image
width, height = picture.size
o_width, o_height = original.size

# Process every pixel
def calcColour(a, b):

    def avg(w, z):
        numb = w + z
        return round(numb / 2)
    return [avg(a[0], b[0]), avg(a[1], b[1]), avg(a[2], b[2])]
def createPixel(newcolour):
    picture2 = Image.open("./images/***REMOVED***")
    array = np.array(picture2)
    for x in range(len(array[0][0])):
        for y in range(len(array[0])):
            current_color = array[x][y]
            ####################################################################
            # Change Pixel Colour
            ####################################################################
            array[x][y] = calcColour(current_color, newcolour)
    return Image.fromarray(np.uint8(array))
    #picture.show()
final = Image.new('RGB', (picture.height * original.height, picture.width * original.width))
start = [0, 0]

for x in range(int(o_width)):
    print(str(round(int(x) / original.width * 100)) + "% Complete")
    for y in range(int(o_height)):
        final.paste(createPixel(original.getpixel((x, y))), (start[0], start[1]))
        #final.paste(createPixel((255, 0, 128)), (start[0], start[1]))
        start[1] += height
    start[1] = 0
    start[0] += width
print("Saving...")
final.save("./output.png")
print("Successfully Saved As output2.png")