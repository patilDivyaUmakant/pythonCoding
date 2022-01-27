import cv2
import pandas as pd
img = cv2.imread("colorpic.jpg")
# print(img)
index = ["COLOR","COLOR_NAME","HEX","R","G","B"]
csv = pd.read_csv("colors.csv",names = index,header = None)
# print (csv)
print (csv.head(10))
print(csv.loc[0,"R"])
print(csv.loc[0,"G"])
print(csv.loc[5,"B"])
cv2.namedWindow("COOR DETECTOR")
while True :
    cv2.imshow("COLOR DETECTOR",img)
    if cv2.waitKey(1) == ord("z") :
        break
cv2.destroyAllWindows()