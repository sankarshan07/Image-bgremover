from rembg import remove
import easygui
from PIL import Image

img =Image.open()   #add image 
output = remove(img)
output.save("")  # add image name to be saved
#

