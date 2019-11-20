import cv2
import os

vod_filename = 'ms33.mp4'
img_prefix = 'ms33'

vod = cv2.VideoCapture('data/video/' + vod_filename) 
fps = 60

framecount = 0

st_template = cv2.imread('data/templates/st.png', cv2.COLOR_BGR2GRAY)
ge_template = cv2.imread('data/templates/ge.png', cv2.COLOR_BGR2GRAY)

#game_end_template = cv2.imread('samples/game_end.png')

#detecting the hyphen (or any of the stock number updates) doesn't work for doubles!
#hyphen position values
roi_x1 = 590
roi_y1 = 285
roi_x2 = 690
roi_y2 = 340

wait = 120
last = 0

while True:

    success,frame = vod.read()

    if not success:
        break

    framecount += 1
    if framecount % 1000 == 0:
        print(framecount)
    
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(frame_gray, (roi_x1, roi_y1), (roi_x2, roi_y2), (255,0,0), 2)
    roi = cv2.Canny(frame_gray[roi_y1:roi_y2,roi_x1:roi_x2],100,200)
    frame_gray[roi_y1:roi_y2,roi_x1:roi_x2] = roi

    st_res = cv2.matchTemplate(roi,st_template,cv2.TM_CCOEFF)
    _, st_max, _, _ = cv2.minMaxLoc(st_res)

    ge_res = cv2.matchTemplate(roi,ge_template,cv2.TM_CCOEFF)
    _, ge_max, _, _ = cv2.minMaxLoc(ge_res)

    if (st_max > 20024226 or ge_max > 16273518) and framecount > last+wait:
        print(framecount)
        last = framecount
        time = int(framecount / 60)
        cv2.imwrite('data/output/' + img_prefix + '_' + str(time) + '.png', frame)

    #if framecount == 10550:

    #    print(framecount)
    #    cv2.imshow('FRAME', frame_gray)
    #    cv2.waitKey()