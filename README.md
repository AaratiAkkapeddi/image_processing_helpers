# image_processing_helpers
helpers for processing/preparing images to then be used as GAN training data.

These are essentially tweaked versions of scripts from [Adrian Rosebrock](https://www.pyimagesearch.com/)
that I use in my personal practice to process images for GAN

- video_to_frames.py -- splits video into individual image frames
- video_to_faces.py -- splits video into individual image frames and then crops faces from these frames
- align_faces.py -- uses [Adrian Rosebrock's code](https://www.pyimagesearch.com/2017/05/22/face-alignment-with-opencv-and-python/) to crop and align faces from photos
- flip.py -- duplicates and flips (horizontally) images in a folder (for augmenting small data)
- resize.py -- will resize to the right dimensions for GAN (from [Eric Kleppen's GAN tutorial](https://medium.com/codex/how-to-train-stylegan2-ada-in-colab-using-instagram-images-7ff552667a20))