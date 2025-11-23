# SEGMENTATION
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT-2\\image\\birds.png')
height, width, channel = im.shape

# seed points
first_bird_seed=(im[120,268])
# 30,34,43
second_bird_seed=(im[185,224])
# 30,38,40
tail_in_seed=(im[158,258])
# 95,99,82
tail_out_seed=(im[159,249])
# 199,203,202

sky_seed=(im[177,300])
# 80,146,180
seed_arr=[first_bird_seed,second_bird_seed,tail_in_seed,tail_out_seed,sky_seed]

for i in seed_arr:
    print(i)
print(second_bird_seed[0],second_bird_seed[1],second_bird_seed[2])

# input()

# r_values = []
file1 = open("image_segmentation\\img2\\text_files\\labeling.txt", "w")


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
             label = "fb"
         elif min_index == 1:
             label = "lb"
         elif min_index == 2:
             label = "ti"
         elif min_index == 3:
             label = "to"
         elif min_index == 4:
             label = "s"
         file1.write(str(y)+","+str(x) +"    BGR:"+str(pixel_value) +"   " + label + "\n")
         min_dis.clear()

         
# cv2.imshow(" Image", im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()                
 
        

plt.imshow(im)
plt.show()