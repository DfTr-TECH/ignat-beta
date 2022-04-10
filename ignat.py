import cv2 
import numpy as np
import RPi.GPIO as pigpio

x_red = 0
y_red = 0
x_white = 0
y_white = 0
x_line = 0 
y_line = 0


pigpio.setmode(pigpio.BCM)
pigpio.setup(22, pigpio.OUT)
pigpio.setup(23, pigpio.OUT)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

    
high_red = np.array((255, 105, 105), np.uint8)
low_red = np.array((160, 0, 0), np.uint8)

  
high_white = np.array((190, 190, 190), np.uint8)
low_white = np.array((130, 130, 130), np.uint8)
cap.set(3, 480)
cap.set(4, 640)

while True:
  
    ret, frame = cap.read()
   
    if not ret:
        print('oops')
        break

    preout= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out_line = cv2.inRange(preout, low_white, high_white)
    
    out_red = cv2.inRange(preout, low_red, high_red)
    
    moments = cv2.moments(out_red, 1)
	
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']
   
   
    if dArea > 150:
        x_red = int(dM10/dArea)
        y_red = int(dM01/dArea)
        
    cv2.circle(frame, (x_red,y_red), 10, (255, 0, 0), -1) 
    moments2 = cv2.moments(out_line, 1)
     
    y_white = moments2['m01']
    x_white = moments2['m10']
    s = moments2['m00']

    if s > 100:
        x_line = int(x_white/s)
        y_line = int(y_white/s)
    cv2.circle(frame, (x_line,y_line), 15, (255, 255, 255), -1)
    
    #cv2.imshow('-', frame)
    
 
    #if x_red > 330 and x_red < 380:
    #    pigpio.output(22, 0)
    #    pigpio.output(23, 0)

#        playsound('voice/crasny cvet.mp3')
      #  break
    pigpio.output(22, 0)
    pigpio.output(23, 0)      

    if x_red < 270:
        pigpio.output(22, 1)
        pigpio.output(23, 0)

    if x_red > 270:
        pigpio.output(22, 0)
        pigpio.output(23, 1)
        
    print(x_line)
    if cv2.waitKey(5) == ord('q'): 
        break


#playsound('voice/vixod.mp3')

cap.release()
cv2.destroyAllWindows()
