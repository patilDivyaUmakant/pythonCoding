import cv2
import dlib
vs = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
while True :
    ret,frame = vs.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces : 
        print(face)
        print (face.left())
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        # cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),4)
        shape = predictor(gray,face)
        # for n in range(0,68) :  
        #     x = shape.part(n).x
        #     y = shape.part(n).y
        #     cv2.circle(frame,(x,y),5,(150,233,100),-1)
        top_nose = (shape.part(29).x , shape.part(29).y)
        cv2.circle(frame,top_nose,15,(0,0,255),-1)
    cv2.imshow("SNAPfilters",frame)
    if cv2.waitKey(1) == ord("z") :
        break
vs.release()
cv2.destroyAllWindows()

