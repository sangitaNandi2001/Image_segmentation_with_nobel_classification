import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT-2\\image\\elephant_coloured.png')

height, width, channel = im.shape


file1 = open("spatial segmentation\\img1\\clr__labeling.txt", "w")


for y in range(height):
     for x in range(width):
         pixel_value = (im[y, x])
         b, g, r = pixel_value
         b=pixel_value[0]  
         g=pixel_value[1]  
         r=pixel_value[2]  

         
          
         if [b,g,r] == [232,162,0]:
              label="s"
         elif  [b,g,r]  == [ 76 , 177 ,  34] :
              label="f"
         elif  [b,g,r]  == [0, 0, 0]:
              label = "e"
         elif  [b,g,r]  == [  0 ,242 ,255]:
              label = "t"
         else :
              label ="o"

         
         file1.write(str(pixel_value)+" "+label+ "\n")



cv2.imshow(" Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()