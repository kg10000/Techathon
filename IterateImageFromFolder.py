
import cv2
"""count=0
vidcap = cv2.VideoCapture('demo.mp4')
while 20:
      image = vidcap.read()
      print("Type of image is ",type(image))
      cv2.imwrite('C:/Users/DELL/Techathon/Automatic_Number_Plate_Detection_Recognition_YOLOv8/Scanned_images/ram_'+str(count)+".jpg",image)
      count+=1  
 """

import gradio as gr

def greet(name):
    return "Hello "+name + "!"

iface = gr.Interface(fn=greet,inputs="text",outputs="text")
iface.launch
cv2.waitKey(0)

