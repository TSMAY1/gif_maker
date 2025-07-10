import imageio.v3 as iio

filenames = []

images = []


for filename in filenames:
    images.append(iio.imread(filename))

    iio.imwrite("export.gif", images, duration = 500, loop = 0)