import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT\\image\\sea_coloured.jpg')

height, width, channel = im.shape


file1 = open("spatial segmentation\\img5\\clr__labeling.txt", "w")


for y in range(height):
     for x in range(width):
         pixel_value = (im[y, x])
         b, g, r = pixel_value
         b=pixel_value[0]  
         g=pixel_value[1]  
         r=pixel_value[2]  

         
         if [b,g,r] == [0,0,0]:
              label="fs"
         
         elif  [b,g,r]  == [0, 242, 254]:
              label = "sea"
         elif  [b,g,r]  == [  232 ,163 ,0]:
              label = "sky"
         else:
              label ="o"
        

         
         file1.write(str(pixel_value)+" "+label+ "\n")



cv2.imshow(" Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()