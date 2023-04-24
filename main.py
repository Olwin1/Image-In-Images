# Import the necessary libraries
from PIL import Image
import numpy as np

# Open the input images
picture = Image.open("./images/smaller_image.png")
original = Image.open("./images/larger_image.png")

# Get the size of the input images
width, height = picture.size
o_width, o_height = original.size

# Define a function to calculate the color of each pixel
def calcColour(a, b):

    # Define a function to average two values
    def avg(w, z):
        numb = w + z + z
        return round(numb / 3)
    
    # Calculate the average of the RGB values of the two input pixels
    return [avg(a[0], b[0]), avg(a[1], b[1]), avg(a[2], b[2]), 255]

# Define a function to create a new pixel based on a given color
def createPixel(newcolour):
    
    # Convert the input image to a numpy array for faster processing
    array = np.array(picture)
    
    # Iterate over every pixel in the image and apply the new color
    for x in range(len(array[0][0])):
        for y in range(len(array[0])):
            current_color = array[x][y]
            array[x][y] = calcColour(current_color, newcolour)
    
    # Convert the numpy array back to an image and return it
    return Image.fromarray(np.uint8(array))

# Create a new blank image with the dimensions of the combined images
final = Image.new('RGB', (picture.width * original.width, picture.height * original.height))

# Define a starting point for pasting the new pixels
start = [0, 0]

# Iterate over every pixel in the original image
for x in range(int(o_width)):
    print(str(round(int(x) / original.width * 100)) + "% Complete")
    for y in range(int(o_height)):
        
        # Calculate the new pixel based on the color of the current pixel in the original image
        new_pixel = createPixel(original.getpixel((x, y)))
        
        # Paste the new pixel onto the final image at the current position
        final.paste(new_pixel, (start[0], start[1]))
        
        # Move the position down by the height of the input image
        start[1] += height
    
    # Reset the position to the top and move it over by the width of the input image
    start[1] = 0
    start[0] += width

# Save the final image to disk
print("Saving...")
final.save("./output.png")
print("Successfully Saved As output.png")
