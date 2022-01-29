from re import X
import cv2
import pandas as pd
r = g = b = x_pos = y_pos = 0
clicked = False
img = cv2.imread("colorpic.jpg")
# print(img)
index = ["COLOR","COLOR_NAME","HEX","R","G","B"]
csv = pd.read_csv("colors.csv",names = index,header = None)
# print (csv)
# print (csv.head(10))
# print(csv.loc[0,"R"])
# print(csv.loc[0,"G"])
# print(csv.loc[5,"B"])
def draw_fun(event,x,y,flags,params) : 
    if event == cv2.EVENT_LBUTTONDBLCLK : 
        global r,g,b,x_pos,y_pos,clicked
        clicked = True
        x_pos = x
        y_pos = y
        print(x,y)
        b,g,r = img[y,x]
        print (type(b),g,r)
        b = int(b)
        g = int(g)
        r = int(r)

def getColorName(R,G,B) : 
    minimum = 100
    for i in range(len(csv)) : 
        d = abs(R - int(csv.loc[i,"R"])) + abs(G - int(csv.loc[i,"G"])) + abs(B - int(csv.loc[i,"B"]))
        if d <= minimum :
            minimum = d
            cname = csv.loc[i,"COLOR_NAME"]

    return cname


# print (getColorName(0,0,0))

cv2.namedWindow("COLOR DETECTOR")
cv2.setMouseCallback("COLOR DETECTOR", draw_fun)
while True :
    cv2.imshow("COLOR DETECTOR",img)
    if clicked :
        cv2.rectangle(img,(20,20),(800,60),(b,g,r),-1)
        text = getColorName(r,g,b) + " R = "+ str(r) + " G = "+ str(g) + " B = "+ str(b) 
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2)
    if cv2.waitKey(1) == ord("z") :
        break
cv2.destroyAllWindows()