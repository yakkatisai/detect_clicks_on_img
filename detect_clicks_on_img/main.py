import cv2
import numpy as np

circles=np.zeros((4,2),np.int)
counter =0

def mousePoints(event,x,y,flags,params):
    global counter
    if event==cv2.EVENT_LBUTTONDOWN:
        circles[counter]=x,y
        counter=counter+1
        print(circles)

img= cv2.imread('img.png')
while 1:
    img=cv2.resize(img,(720,640))
    if counter==4:
        print(counter)
        w,h=720,640
        pts1=np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
        matrix=cv2.getPerspectiveTransform(pts1,pts2)
        imgoutput=cv2.warpPerspective(img,matrix,(w,h))
        cv2.imshow("img",imgoutput)
    for x in range(0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),3,(0,255,0),cv2.FILLED)



        '''for x in range(2,3):
            cv2.circle(img1,(int(pts1[x][0]),int(pts1[x][1])),5,(0,0,255),cv2.FILLED)
            print(pts1[x][0],pts1[x][1])'''

    cv2.imshow('orginal',img)
    cv2.setMouseCallback("orginal",mousePoints)
    cv2.waitKey(0)