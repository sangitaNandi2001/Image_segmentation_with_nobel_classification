import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'image\\lastu.png')

height, width, channel = im.shape


file1 = open("image_segmentation\\img6\\clr__labeling.txt", "w")


for y in range(height):
     for x in range(width):
         pixel_value = (im[y, x])
         b, g, r = pixel_value
         b=pixel_value[0]  
         g=pixel_value[1]  
         r=pixel_value[2]  

         
         if [b,g,r] == [35,28,227]:
              label="ls"
         
         elif  [b,g,r]  == [77, 177, 35]:
              label = "key"
         elif  [b,g,r]  == [ 38,127 ,255]:
              label = "book"
        
         else:
              label ="bg"
        

         
         file1.write(str(pixel_value)+" "+label+ "\n")



cv2.imshow(" Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()