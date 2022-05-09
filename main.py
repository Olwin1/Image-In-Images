from PIL import Image
picture = Image.open("./images/***REMOVED***")

# Get the size of the image
width, height = picture.size

# Process every pixel
newcolour = (29, 230, 25)
def calcColour(a, b):
    return (round(a[0] + b[0] / 2), round(a[1] + b[1] / 2), round(a[2] + b[2] / 2))
for x in range(width):
   for y in range(height):
       current_color = picture.getpixel( (x,y) )
       ####################################################################
       # Do your logic here and create a new (R,G,B) tuple called new_color
       ####################################################################
       picture.putpixel( (x,y), calcColour(current_color, newcolour))
picture.show()