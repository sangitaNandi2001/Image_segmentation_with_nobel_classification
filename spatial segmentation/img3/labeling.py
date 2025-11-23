# SEGMENTATION
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT-2\\image\\animal.png')
height, width, channel = im.shape
# function to calculate mean -----------------------------------------------------------------
def mean_calc(arr):
    sum_r=0
    sum_g=0
    sum_b=0
    len_arr=len(arr)

    for i in arr :
        sum_r+=i[0]
        sum_g+=i[1]
        sum_b+=i[2]
    mean_arr = (sum_r/len_arr,sum_g/len_arr,sum_b/len_arr)
    return (mean_arr)


       
# mean_calc(arr)
# -------------------------------------------------------------------------------------


# seed points
field_light_seed=(im[205,107])
# 221,191,121
field_dark_seed=(im[297,81])
# 162,137,96

background_seed=(im[39,243])
# 74,82,71
body_seed=(im[177,263])
# 111,102,73
head_seed=(im[166,173])
# 25,23,10

seed_arr=[field_light_seed,field_dark_seed,background_seed,body_seed,head_seed]

for i in seed_arr:
    print(i)
print(field_dark_seed[0],field_dark_seed[1],field_dark_seed[2])
arr_field_light_seed=[field_light_seed]
arr_field_dark_seed=[field_dark_seed]
arr_background_seed=[background_seed]
arr_body_seed=[body_seed]
arr_head_seed=[head_seed]



# r_values = []
file1 = open("spatial segmentation\\img3\\labeling.txt", "w")


for y in range(height):
     for x in range(width):
         seed_arr=[field_light_seed,field_dark_seed,background_seed,body_seed,head_seed]
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
             label = "fl"
             arr_field_light_seed.append(pixel_value)
             var1 =mean_calc(arr_field_light_seed)
             field_light_seed=var1
         elif min_index == 1:
             label = "fd"
             arr_field_dark_seed.append(pixel_value)
             var2 =mean_calc(arr_field_dark_seed)
             field_dark_seed= var2
         elif min_index == 2:
             label = "bg"
             arr_background_seed.append(pixel_value)
             var3 =mean_calc(arr_background_seed)
             background_seed= var3
         elif min_index == 3:
             label = "body"
             arr_body_seed.append(pixel_value)
             var4 =mean_calc(arr_body_seed)
             body_seed= var4
         elif min_index == 4:
             label = "head"
             arr_head_seed.append(pixel_value)
             var5 =mean_calc(arr_head_seed)
             head_seed= var5
         file1.write(str(y)+","+str(x) +"    BGR:"+str(pixel_value) +"   " + label + "\n")
         min_dis.clear()

         
# cv2.imshow(" Image", im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()                
 
        

plt.imshow(im)
plt.show()