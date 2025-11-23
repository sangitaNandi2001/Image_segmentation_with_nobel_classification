import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT-2\\image\\bird_coloured.png')

height, width, channel = im.shape


file1 = open("spatial segmentation\\img2\\clr__labelling.txt", "w")


for y in range(height):
     for x in range(width):
         pixel_value = (im[y, x])
         r, g, b = pixel_value
         r=pixel_value[0]  
         g=pixel_value[1]  
         b=pixel_value[2]  

         
         if [r,g,b] == [0,0,0]:
              label="fb"
         elif  [r,g,b]  == [ 21, 0 ,  136] :
              label="lb"
         elif  [r,g,b]  == [29, 230, 181]:
              label = "ti"
         elif  [r,g,b]  == [  255 ,255 ,255]:
              label = "to"
         else :
              label ="s"

         
         file1.write(str(pixel_value)+" "+label+ "\n")



cv2.imshow(" Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()