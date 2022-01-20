import cv2
vs = cv2.VideoCapture(0)
while True :
    ret,frame = vs.read()
    cv2.imshow("SNAPfilters",frame)
    if cv2.waitKey(1) == ord("z") :
        break
vs.release()
cv2.destroyAllWindows()

