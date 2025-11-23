import matplotlib.pyplot as plt
import matplotlib.image as img

im = img.imread("D:\\PROJECT-2\\image\\Lena-gray.png")

height, width, channel = im.shape

pixel_values = []
file1 = open("histogram\\text_files\\histo_of_gray.txt", "w")

for y in range(height):
    for x in range(width):
        pixel_value = int(im[y, x][0] * 255)  # Assuming the image is in the range [0.0, 1.0]
        pixel_values.append(pixel_value)

hist = [0 for i in range(256)]

for value in pixel_values:
    # Convert the value to an integer before using it as an index
    value = int(value)
    hist[value] += 1

i = 0
for x in hist:
    file1.write(str(i) + ",")
    file1.write(str(x) + '\n')
    i += 1

file1.close()
