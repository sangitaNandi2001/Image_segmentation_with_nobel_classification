# SEGMENTATION
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT-2\\image\\elephant.jpg')
height, width, channel = im.shape



# function to calculate mean -----------------------------------------------------------------
def mean_calc(arr):
    sum_b=0
    sum_g=0
    sum_r=0
    len_arr=len(arr)

    for i in arr :
        sum_b+=i[0]
        sum_g+=i[1]
        sum_r+=i[2]
    mean_arr = (sum_b/len_arr,sum_g/len_arr,sum_r/len_arr)
    return (mean_arr)


       
# mean_calc(arr)
# -------------------------------------------------------------------------------------


# seed points
field_seed=(im[278,234])
tree_seed=(im[172,256])
ele_seed=(im[228,288])
sky_seed=(im[83,246])
seed_arr=[field_seed,tree_seed,ele_seed,sky_seed]

for i in seed_arr:
    print(i)
print(field_seed[0],field_seed[1],field_seed[2])
arr_field_seed=[field_seed]
arr_tree_seed=[tree_seed]
arr_ele_seed=[ele_seed]
arr_sky_seed=[sky_seed]

# ----------------------------------------------------------------------------------


# r_values = []
file1 = open("spatial segmentation\\img1\\labeling5.txt", "w")


for y in range(height):
     for x in range(width):
         seed_arr=[field_seed,tree_seed,ele_seed,sky_seed]

         pixel_value = (im[y, x])
         b=pixel_value[0] 
         g=pixel_value[1]  
         r=pixel_value[2] 
         

         min_dis=[]
         for i in seed_arr:
            #  print(i)
             
             b1 = np.int8(i[0])
             b = np.int8(pixel_value[0])
             g1 = np.int8(i[1])
             g= np.int8(pixel_value[1])
             r1 = np.int8(i[2])
             r = np.int8(pixel_value[2])

             dist = math.sqrt((b1-b)**2+(g1-g)**2+(r1-r)**2)
            #  print(dist)
             min_dis.append(dist)
        #  print(min_dis)
        #  input()
         min_value = min(min_dis)
         min_index = min_dis.index(min_value)
        
         if min_index == 0:
             label = "f"
             arr_field_seed.append(pixel_value)
             var1 =mean_calc(arr_field_seed)
             field_seed=var1
         elif min_index == 1:
             label = "t"
             arr_tree_seed.append(pixel_value)
             var2 =mean_calc(arr_tree_seed)
             tree_seed= var2
         elif min_index == 2:
             label = "e"
             arr_ele_seed.append(pixel_value)
             var3 =mean_calc(arr_ele_seed)
             ele_seed = var3
         elif min_index == 3:
             label = "s"
             arr_sky_seed.append(pixel_value)
             var4 =mean_calc(arr_sky_seed)
             sky_seed = var4
            
         
        
         file1.write(str(y)+","+str(x) +"    BGR:"+str(pixel_value) +"   " + label + "\n")
         min_dis.clear()
         


         
