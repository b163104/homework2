import numpy as np
import cv2

def changeColor(val):
    pass #do nothing



cv2.namedWindow('img', cv2.WINDOW_NORMAL)

# トラックバーの生成
cv2.createTrackbar('R', 'img', 0, 255, changeColor)
cv2.createTrackbar('G', 'img', 0, 255, changeColor)
cv2.createTrackbar('B', 'img', 0, 255, changeColor)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):
    
    ret, frame = cap.read()
    if not ret: continue
    
    R=cv2.getTrackbarPos('R','img')
    G=cv2.getTrackbarPos('G','img')
    B=cv2.getTrackbarPos('B','img')

    
    v = cv2.getTrackbarPos('value',  # get the value
                           'title')  # of the win
        
                           ## do something by using v
    if(B!=0):
        frame[:,:,0]=B
    elif(G!=0):
        frame[:,:,1]=G
    elif(R!=0):
        frame[:,:,2]=R
    cv2.putText(frame, "red:"+str(R),(20,40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
    cv2.putText(frame, "green:"+str(G),(20,70),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
    cv2.putText(frame, "blue:"+str(B),(20,100),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
    cv2.imshow('title', frame)  # show in the win
                           
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
