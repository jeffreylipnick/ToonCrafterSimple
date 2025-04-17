from tooncrafter.i2v import Image2Video

i2v = Image2Video("src/tooncrafter/new.yaml", result_dir="/tmp/tc-results", resolution='320_512', fp16=True)

image = ... # e.g. numpy.asarray(PIL.Image.open(...))

video_output_path = i2v.get_image(image, "an anime scene", image, steps=20, fs=10)
