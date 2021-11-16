import os
import PIL
from PIL import Image
import argparse
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

def convert_image(filename):
	if (filename.endswith(".jpg") or filename.endswith(".jpeg")) and not filename.startswith("flipped_"):
	    im = Image.open(folder+'/'+ filename)
	    im.transpose(PIL.Image.FLIP_LEFT_RIGHT).save(outdir +'/flipped_' + filename,
	                           'JPEG',
	                           quality_mode='dB',
	                           quality_layers=[41])


for filename in os.listdir(folder):
     convert_image(filename)