# SEGMENTATION
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'image\\juju.jpg')
height, width, channel = im.shape


laptop_sr_seed=(im[88,238])

laptop_key_seed=(im[197,242])
book_seed=(im[220,373])

bg_seed=(im[251,250])

seed_arr=[laptop_sr_seed,laptop_key_seed,book_seed,bg_seed]

# for i in seed_arr:
#     print(i)
# print(first_stone_seed[0],first_stone_seed[1],first_stone_seed[2])





# r_values = []
file1 = open("image_segmentation\\img6\\labeling.txt", "w")


for y in range(height):
     for x in range(width):
         seed_arr=[laptop_sr_seed,laptop_key_seed,book_seed,bg_seed]

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
             label = "ls"
             
         elif min_index == 1:
             label = "key"
             
         elif min_index == 2:
             label = "book"
             
         
         elif min_index == 3:
             label = "bg"
             


         file1.write(str(y)+","+str(x) +"    BGR:"+str(pixel_value) +"   " + label + "\n")
         min_dis.clear()

         
# cv2.imshow(" Image", im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()                
 
        

plt.imshow(im)
plt.show()