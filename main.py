
import camera_detection
import pygame,sys
import cv2
import numpy as np
import time

size=(0,0)
cap=cv2.VideoCapture(0) #0 for 1st webcam
frame_id = 0
def black():
    i=0
    screen=pygame.display.set_mode(size,pygame.FULLSCREEN,pygame.RESIZABLE)
    print("display=",(i+1))
while(True):
    _,frame= cap.read() # 
    print("frame captured")
    frame_id+=1
    if(camera_detection.is_camera_present(frame,frame_id)):
        print("detection unit called")
        black()
    else:
        print("not detected")
        pygame.quit() 
        

