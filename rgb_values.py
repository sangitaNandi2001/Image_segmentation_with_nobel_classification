import matplotlib.pyplot as plt
import matplotlib.image as img


im = img.imread("D:\PROJECT-2\image\lena_color.gif")
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


print(r_values  )
print()
print(g_values )

print()
print(b_values)
# plt.imshow(im)
# plt.show()