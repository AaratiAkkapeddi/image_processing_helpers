#import dependencies 
from PIL import Image
import os, sys
#set file path
path = './output_all_augmented/'
dirs = os.listdir( path )
def resize():
    
    #loop through the images
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            
            #set the output size: 256,256 or 512,512 or 1024,1024
            imResize = im.resize((512,512), Image.ANTIALIAS)
            
            #save the images as image name + resized
            imResize.save('resized/'+item + ' resized.jpg', 'JPEG', quality=100, optimize=True)
#run the funtion
resize()