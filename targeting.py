import cv2
import numpy as np


if __name__ == '__main__':
    def nothing(*arg):
        pass

cv2.namedWindow( "result" )
cv2.namedWindow( "settings" )

cap = cv2.VideoCapture(0)

cv2.createTrackbar('r1', 'settings', 0, 255, nothing)
cv2.createTrackbar('g1', 'settings', 0, 255, nothing)
cv2.createTrackbar('b1', 'settings', 0, 255, nothing)
cv2.createTrackbar('r2', 'settings', 255, 255, nothing)
cv2.createTrackbar('g2', 'settings', 255, 255, nothing)
cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
crange = [0,0,0, 0,0,0]

while True:
    flag, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
    r1 = cv2.getTrackbarPos('r1', 'settings')
    g1 = cv2.getTrackbarPos('g1', 'settings')
    b1 = cv2.getTrackbarPos('b1', 'settings')
    r2 = cv2.getTrackbarPos('r2', 'settings')
    g2 = cv2.getTrackbarPos('g2', 'settings')
    b2 = cv2.getTrackbarPos('b2', 'settings')

  
    h_min = np.array((r1, g1, b1), np.uint8)
    h_max = np.array((r2, g2, b2), np.uint8)

    
    thresh = cv2.inRange(hsv, h_min, h_max)

    cv2.imshow('result', thresh) 
 
    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()
