import cv2 
import numpy as np
import pigpio

x_red = 0
y_red = 0
x_bar = 0
y_bar = 0

l = 0
r = 0 

pi1 = pigpio.pi()
cap = cv2.VideoCapture(0) # 0 - main camera, 1 - qr camera

if not cap.isOpened():
    print("Cannot open camera")
    exit()

#RGB
#high_red = np.array((255, 105, 105), np.uint8)
#low_red = np.array((160, 0, 0), np.uint8)

#high_green = np.array((64, 255, 64), np.uint8)
#low_green = np.array((0, 115, 0), np.uint8)

#HSV
    
high_red = np.array((255, 255, 255), np.uint8)
low_red = np.array((167, 123, 169), np.uint8)

high_green = np.array((79, 255, 255), np.uint8)
low_green = np.array((0, 68, 204), np.uint8)

cap.set(3, 480)
cap.set(4, 640)

while True:
  
    ret, frame = cap.read()
   
    if not ret:
        print('oops')
        break

    preout= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    out_green = cv2.inRange(preout, low_green, high_green)
    out_red = cv2.inRange(preout, low_red, high_red)
    
    moments = cv2.moments(out_red, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']
   
    if dArea > 150:
        x_red = int(dM10/dArea)
        y_red = int(dM01/dArea)
        
    cv2.circle(frame, (x_red,y_red), 10, (50, 50, 255), -1) 
    
    
    moments2 = cv2.moments(out_green, 2)
    y_green = moments2['m01']
    x_green = moments2['m10']
    s = moments2['m00']

    if s > 100:
        x_bar = int(x_green/s)
        y_bar = int(y_green/s)
    cv2.circle(frame, (x_bar,y_bar), 15, (25, 255, 55), -1)
    
    #cv2.imshow('red obj', out_red)
    #cv2.imshow('yellow', out_green)
    #cv2.imshow('output stream', frame)
 
    if x_bar > 330 and x_bar < 380:
        #pigpio.output(5, 0)
        #pigpio.output(5, 0)
        #l = 0
        r = 0

        #pigpio.output(22, 0)
        #pigpio.output(23, 0)
        #break
    
    if x_red > 270:
        #pigpio.output(22, 1)
        #pigpio.output(23, 0)
        pi1.write(22, 1)
        pi1.write(23, 0)
        #r += 5
        #l = 0
        
    if x_red < 270:
        #pigpio.output(22, 0)
        #pigpio.output(23, 1)
	pi1.write(22, 0)
	pi1.write(23, 1)
        #l += 5
        #r = 0
        
    #pi1.set_PWM_dutycycle(22, l)
    #pi1.set_PWM_dutycycle(23, r)
    if l > 200:
        l = 200
    if r > 200:
        r = 200

    print(x_red)
    if cv2.waitKey(5) == ord('q'): 
        #cv2.imwrite('green.jpg', out_green)
        break


#playsound('voice/vixod.mp3')
l = 0
r = 0
cap.release()
cv2.destroyAllWindows()
