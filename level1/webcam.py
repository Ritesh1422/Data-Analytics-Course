import cv2

cam=cv2.vedioCapture(0)

while cam.isOpened():
    ststus,image=cam.read()
    cv2.imshow('scaled',img_scaled)
    