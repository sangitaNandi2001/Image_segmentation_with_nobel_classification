# SEGMENTATION
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT\\image\\moutain.jpg')
height, width, channel = im.shape

# seed points
sky_seed=(im[56,205])
# 227,211,159
first_moun_seed=(im[121,226])
# 163,159,121
second_moun_seed=(im[140,283])
# 120,124,91
third_moun_seed=(im[188,211])
# 89,94,71
field_seed=(im[280,160])
# 16,17,12


seed_arr=[sky_seed,first_moun_seed,second_moun_seed,third_moun_seed,field_seed]

for i in seed_arr:
    print(i)
print(sky_seed[0],sky_seed[1],sky_seed[2])



# r_values = []
file1 = open("image_segmentation\\img4\\text_files\\labeling.txt", "w")


for y in range(height):
     for x in range(width):
         pixel_value = (im[y, x])
         b=pixel_value[0] 
         g=pixel_value[1]  
         r=pixel_value[2] 
         

         min_dis=[]
         for i in seed_arr:
            #  print(i[0],r)
            #  print(i[0]-r)
            #  input()
             b1 = np.int8(i[0])
             b = np.int8(pixel_value[0])
             g1 = np.int8(i[1])
             g= np.int8(pixel_value[1])
             r1 = np.int8(i[2])
             r = np.int8(pixel_value[2])

             dist = math.sqrt((b1-b)**2+(g1-g)**2+(r1-r)**2)
            #  print(dist)
            #  print(dist)
             min_dis.append(dist)
        #  print(len(min_dis))
        #  input()
        #  for i in min_dis:
        #      print(i)
        #  input()
         min_value = min(min_dis)
        #  print(min_value)
        #  input()

         min_index = min_dis.index(min_value)
        #  print(min_index)
        #  input()
         if min_index == 0:
             label = "s"
         elif min_index == 1:
             label = "fm"
         elif min_index == 2:
             label = "sm"
         elif min_index == 3:
             label = "tm"
         elif min_index == 4:
             label = "f"
         
         file1.write(str(y)+","+str(x) +"    BGR:"+str(pixel_value) +"   " + label + "\n")
         min_dis.clear()

         
# cv2.imshow(" Image", im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()                
 
        
plt.imshow(im)
plt.show()