# SEGMENTATION
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT-2\\image\\birds.png')
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

# -------------------------------------------------------------------------------------

# seed points
first_bird_seed=(im[120,268])
# 30,34,43
second_bird_seed=(im[185,224])
# 30,38,40
tail_in_seed=(im[153,245])
# 95,99,82
tail_out_seed=(im[160,250])
# 199,203,202

sky_seed=(im[51,261])
# 80,146,180
seed_arr=[first_bird_seed,second_bird_seed,tail_in_seed,tail_out_seed,sky_seed]

for i in seed_arr:
    print(i)
# print(second_bird_seed[0],second_bird_seed[1],second_bird_seed[2])
print("seed fierst")
arr_first_bird_seed_seed=[first_bird_seed]
arr_second_bird_seed=[second_bird_seed]
arr_tail_in_seed=[tail_in_seed]
arr_tail_out_seed=[tail_out_seed]

arr_sky_seed=[sky_seed]
# input()

# r_values = []
file1 = open("spatial segmentation\\img2\\labeling5.txt", "w")


for y in range(height):
     for x in range(width):
         seed_arr=[first_bird_seed,second_bird_seed,tail_in_seed,tail_out_seed,sky_seed]

         pixel_value = (im[y, x])
         r=pixel_value[0] 
         g=pixel_value[1]  
         b=pixel_value[2] 
         

         min_dis=[]
         for i in seed_arr:
            #  print(i[0],r)
            #  print(i[0]-r)
            #  input()
             r1 = np.int32(i[0])
             r = np.int32(pixel_value[0])
             g1 = np.int32(i[1])
             g= np.int32(pixel_value[1])
             b1 = np.int32(i[2])
             b = np.int32(pixel_value[2])
             

             dist = math.sqrt((r1-r)**2+(g1-g)**2+(b1-b)**2)
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
             arr_first_bird_seed_seed.append(pixel_value)
             var1 =mean_calc(arr_first_bird_seed_seed)
             first_bird_seed = var1
         elif min_index == 1:
             label = "lb"
             arr_second_bird_seed.append(pixel_value)
             var2 =mean_calc(arr_second_bird_seed)
             second_bird_seed = var2
         elif min_index == 2:
             label = "ti"
             arr_tail_in_seed.append(pixel_value)
             var3 =mean_calc(arr_tail_in_seed)
             tail_in_seed = var3
         elif min_index == 3:
             label = "to"
             arr_tail_out_seed.append(pixel_value)
             var4 =mean_calc(arr_tail_out_seed)
             tail_out_seed = var4
         elif min_index == 4:
             label = "s"
             arr_sky_seed.append(pixel_value)
             var5 =mean_calc(arr_sky_seed)
             sky_seed = var5
         file1.write(str(y)+","+str(x) +"    RGB:"+str(pixel_value) +"   " + label + "\n")
         min_dis.clear()
        #  seed_arr.clear()
        #  for lu in arr_first_bird_seed_seed:
        #      print (lu)
        #  print("arr_first_bird_seed_seed")
        #  for lu in arr_second_bird_seed:
        #      print (lu)
        #  print("arr_second_bird_seed")
        #  for lu in arr_tail_in_seed:
        #      print (lu)
        #  print("arr_tail_in_seed")
        #  for lu in arr_tail_out_seed:
        #      print (lu)
        #  print("arr_tail_out_seed")
        #  for lu in arr_sky_seed:
        #      print (lu)
        #  print("arr_sky_seed")
         
        #  print('------------------------')
        
        #  print(min_value)
        #  for i in seed_arr:
        #      print(i )
        #  print("==============")

        #  input()


         
# cv2.imshow(" Image", im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()                
 
        

plt.imshow(im)
plt.show()