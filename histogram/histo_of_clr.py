import matplotlib.pyplot as plt
import matplotlib.image as img

im = img.imread("D:\\PROJECT-2\\image\\lena_color.gif")

height, width, channel = im.shape


r_values = []
g_values = []
b_values = []


for y in range(height):
    for x in range(width):
       pixel_value = (im[y, x])
       r=pixel_value[0] 
       g=pixel_value[1] 
       b=pixel_value[2] 
       r_values.append(r)
       g_values.append(g)
       b_values.append(b)

hist_r = [0 for i in range(256)]
file1 = open("histogram\\text_files\\histo_of_r.txt", "w")
for value in r_values:
    # Convert the value to an integer before using it as an index
    
    hist_r[value] += 1

i = 0
for x in hist_r:
    file1.write(str(i) + ",")
    file1.write(str(x) + '\n')
    i += 1

file1.close()

hist_g = [0 for i in range(256)]
file2 = open("histogram\\text_files\\histo_of_g.txt", "w")
for value in g_values:
    # Convert the value to an integer before using it as an index
    
    hist_g[value] += 1

i = 0
for x in hist_g:
    file2.write(str(i) + ",")
    file2.write(str(x) + '\n')
    i += 1

file2.close()

hist_b = [0 for i in range(256)]
file3= open("histogram\\text_files\\histo_of_b.txt", "w")
for value in b_values:
    # Convert the value to an integer before using it as an index
    
    hist_b[value] += 1

i = 0
for x in hist_b:
    file3.write(str(i) + ",")
    file3.write(str(x) + '\n')
    i += 1

file3.close()
