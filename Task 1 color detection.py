# Dataset link: "https://www.kaggle.com/datasets/adityabhndari/color-detection-data-set?resource=download"
import subprocess
subprocess.run(["pip", "install", "opencv-python", "pandas",  "matplotlib"])
import cv2 #used to process images and videos to identify objects
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img_path=r'C:/Users/swarn/Downloads/archive (2)/colorpic.jpg'
img=mpimg.imread(img_path)

plt.imshow(img)
plt.axis('off')
plt.show()

index =['color','color_name','hex','R','G','B'] #hex=hexadecimal value of color
Data=pd.read_csv("C:/Users/swarn/Downloads/archive (2)/colors.csv",  names=index)
Data.head(10)

clicked = False
r = g = b = xpos = ypos = 0


def get_color_name(R, G, B):
    minimum = 1000
    for i in range(len(Data)):
        t = abs(R - int(Data.loc[i, 'R'])) + abs(G - int(Data.loc[i, 'G'])) + abs(B - int(Data.loc[i, 'B']))
        if t <= minimum:
            minimum = t
            nname = Data.loc[i, 'color_name']
    return nname


print(get_color_name(250, 250, 250))
print(get_color_name(250, 0, 0))


def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, b, g, r, xpos, ypos
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)
print(clicked, b, g, r, xpos, ypos)


while True:
    cv2.imshow('image', img)
    if clicked:
        cv2.rectangle(img, (20,20),  (600,60),(b,g,r), -1)
        text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)
        if r+g+b >=600:
            cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()