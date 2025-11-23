# SEGMENTATION
from matplotlib import pyplot as plt
import matplotlib.image as img  

import math
im = img.imread(r'D:\\PROJECT-2\\image\\elephant.jpg')
height, width, channel = im.shape

# seed points
field_seed=(im[278,234])
tree_seed=(im[172,256])
ele_seed=(im[228,288])
sky_seed=(im[83,246])
seed_arr=[field_seed,tree_seed,ele_seed,sky_seed]

for i in seed_arr:
    print(i)
print(field_seed[0],field_seed[1],field_seed[2])



# r_values = []
file1 = open("image_segmentation\\img1\\text_files\\labeling.txt", "w")


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
             b1 = int(i[0])
             b = int(pixel_value[0])
             g1 = int(i[1])
             g= int(pixel_value[1])
             r1 = int(i[2])
             r = int(pixel_value[2])

             dist = int(math.sqrt((b1-b)**2+(g1-g)**2+(r1-r)**2))
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
             label = "f"
         elif min_index == 1:
             label = "t"
         elif min_index == 2:
             label = "e"
         elif min_index == 3:
             label = "s"
         file1.write(str(y)+","+str(x) +"    BGR:"+str(pixel_value) +"   " + label + "\n")
         min_dis.clear()

         
# cv2.imshow(" Image", im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()                
 
        

plt.imshow(im)
plt.show()