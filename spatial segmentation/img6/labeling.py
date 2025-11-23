# SEGMENTATION
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'image\\juju.jpg')
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


laptop_sr_seed=(im[88,238])

laptop_key_seed=(im[197,242])
book_seed=(im[220,373])

bg_seed=(im[251,250])

seed_arr=[laptop_sr_seed,laptop_key_seed,book_seed,bg_seed]

# for i in seed_arr:
#     print(i)
# print(first_stone_seed[0],first_stone_seed[1],first_stone_seed[2])

arr_laptop_sr_seed=[laptop_sr_seed]
arr_laptop_key_seed=[laptop_key_seed]

arr_book_seed=[book_seed]

arr_bg_seed=[bg_seed]
for i in seed_arr:
    print(i )





# r_values = []
file1 = open("spatial segmentation\\img6\\labeling.txt", "w")


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
             arr_laptop_sr_seed.append(pixel_value)
             var1 =mean_calc(arr_laptop_sr_seed)
             laptop_sr_seed=var1
         elif min_index == 1:
             label = "key"
             arr_laptop_key_seed.append(pixel_value)
             var2 =mean_calc(arr_laptop_key_seed)
             laptop_key_seed=var2
         elif min_index == 2:
             label = "book"
             arr_book_seed.append(pixel_value)
             var3 =mean_calc(arr_book_seed)
             book_seed=var3
         
         elif min_index == 3:
             label = "bg"
             arr_bg_seed.append(pixel_value)
             var4 =mean_calc(arr_bg_seed)
             bg_seed=var4
             print(seed_arr)
             #  input()
         for lu in arr_laptop_sr_seed:
             print (lu)
         print("arr_laptop_sr_seed---------------")
         for lu in arr_laptop_key_seed:
             print (lu)
         print("arr_laptop_key_seed---------------")
         for lu in arr_book_seed:
             print (lu)
         print("arr_book_seed---------------")
         for lu in arr_bg_seed:
             print (lu)
         print("arr_bg_seed----------------")
         
         
         print('------------------------')
        
         print(min_value)
         for i in seed_arr:
             print(i )
         print("==============")

         input()


         file1.write(str(y)+","+str(x) +"    BGR:"+str(pixel_value) +"   " + label + "\n")
         min_dis.clear()


         
# cv2.imshow(" Image", im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()                
 
        

plt.imshow(im)
plt.show()