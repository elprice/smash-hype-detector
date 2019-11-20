import cv2
import os

vod = cv2.VideoCapture('samples/test_footage.mp4') 

framecount = 0

#stock_taken_template = cv2.imread('samples/stock_taken.png')
#game_end_template = cv2.imread('samples/game_end.png')

st_x1 = 100
st_y1 = 100
st_x2 = 950
st_y2 = 600


while True:

    success,frame = vod.read()

    if not success:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.rectangle(frame_gray, (st_x1, st_y1), (st_x2, st_y2), (255,0,0), 2)

    framecount += 1

    if framecount < 5900 and framecount > 5750 and framecount % 20 == 0:
        print(framecount)
        cv2.imshow('FRAME', frame_gray)
        cv2.waitKey()