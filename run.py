import numpy as np
from PIL import Image
from tooncrafter.i2v import Image2Video

i2v = Image2Video("src/tooncrafter/new.yaml", result_dir="/tmp/tc-results", resolution='320_512', fp16=True)

image1 = np.asarray(Image.open("~/assets/tooncrafter/74906_1462_frame1.png"))
image2 = np.asarray(Image.open("~/assets/tooncrafter/74906_1462_frame3.png"))

video_output_path = i2v.get_image(image1, "an anime scene", image2, steps=5, fs=1)
