import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT-2\\image\\coloured_animal.png')

height, width, channel = im.shape


file1 = open("spatial segmentation\\img3\\clr__labeling.txt", "w")


for y in range(height):
     for x in range(width):
         pixel_value = (im[y, x])
         b, g, r = pixel_value
         b=pixel_value[0]  
         g=pixel_value[1]  
         r=pixel_value[2]  

         
         if [b,g,r] == [29,230,181]:
              label="fl"
         elif  [b,g,r]  == [ 76 , 177 ,  34] :
              label="fd"
         elif  [b,g,r]  == [0, 0, 0]:
              label = "bg"
         elif  [b,g,r]  == [  21 ,0 ,136]:
              label = "body"
         elif  [b,g,r]  == [  36 ,28 ,227]:
              label ="head"
         else:
              label ="o"
              

         
         file1.write(str(pixel_value)+" "+label+ "\n")



cv2.imshow(" Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()