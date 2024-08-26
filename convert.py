from PIL import Image
import pillow_heif
import os
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
    if (filename.endswith(".heic") or filename.endswith(".HEIC")):
        heif_file = pillow_heif.read_heif(folder+'/'+ filename)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            ).save(outdir +'/' + filename,
                               'JPEG',
                               quality_mode='dB',
                               quality_layers=[41])
    elif (filename.endswith(".png") or filename.endswith(".PNG") or filename.endswith(".JPG") or filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".JPEG")):
        im = Image.open(folder+'/'+ filename)
        image = im.convert('RGB')
        image.save(outdir +'/' + filename,
                               'JPEG',
                               quality_mode='dB',
                               quality_layers=[41])



for filename in os.listdir(folder):
     convert_image(filename)




    