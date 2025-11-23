import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT\\image\\mountain_coloured.png')

height, width, channel = im.shape


file1 = open("image_segmentation\\img4\\text_files\\clr__labeling.txt", "w")


for y in range(height):
     for x in range(width):
         pixel_value = (im[y, x])
         b, g, r = pixel_value
         b=pixel_value[0]  
         g=pixel_value[1]  
         r=pixel_value[2]  

         
         if [b,g,r] == [0,0,0]:
              label="f"
         elif  [b,g,r]  == [ 76 , 177 ,34] :
              label="s"
         elif  [b,g,r]  == [201, 174, 255]:
              label = "fm"
         elif  [b,g,r]  == [  76 ,228 ,239]:
              label = "sm"
         elif  [b,g,r]  == [  36 ,28 ,227]:
              label = "tm"
         else:
              label ="o"
         

         
         file1.write(str(pixel_value)+" "+label+ "\n")



cv2.imshow(" Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()