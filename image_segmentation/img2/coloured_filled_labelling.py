import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT-2\\image\\bird_coloured.png')

height, width, channel = im.shape


file1 = open("image_segmentation\\img2\\text_files\\clr__labeling.txt", "w")


for y in range(height):
     for x in range(width):
         pixel_value = (im[y, x])
         b, g, r = pixel_value
         b=pixel_value[0]  
         g=pixel_value[1]  
         r=pixel_value[2]  

         
         if [b,g,r] == [0,0,0]:
              label="fb"
         elif  [b,g,r]  == [ 21, 0 ,  136] :
              label="lb"
         elif  [b,g,r]  == [29, 230, 181]:
              label = "ti"
         elif  [b,g,r]  == [  255 ,255 ,255]:
              label = "to"
         else :
              label ="s"

         
         file1.write(str(pixel_value)+" "+label+ "\n")



cv2.imshow(" Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()