import os
import PIL
from PIL import Image

def convert_image(filename):
	if (filename.endswith(".jpg") or filename.endswith(".jpeg")) and not filename.startswith("flipped_"):
	    im = Image.open('./output_all_augmented/'+ filename)
	    im.transpose(PIL.Image.FLIP_LEFT_RIGHT).save('./output_all_augmented/flipped_' + filename,
	                           'JPEG',
	                           quality_mode='dB',
	                           quality_layers=[41])


for filename in os.listdir('./output_all_augmented'):
     convert_image(filename)