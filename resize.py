#import dependencies 
from PIL import Image
import os, sys
import argparse
#set file path
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--indir', type=str, required=True)
parser.add_argument('--outdir', type=str, required=True)
# Print "Hello" + the user input argument
# Parse the argument
args = parser.parse_args()
print('processing images from', args.indir)
print('saving images to', args.outdir)
folder = args.indir
outdir = args.outdir
if not os.path.isdir(outdir):
	os.mkdir(""+outdir)

path = folder +"/"
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
            imResize.save(outdir+'/'+item + ' resized.jpg', 'JPEG', quality=100, optimize=True)
#run the funtion
resize()