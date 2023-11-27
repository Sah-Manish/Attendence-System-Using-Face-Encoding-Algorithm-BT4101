import cv2
import numpy as np
import face_recognition
import os
import datetime
import logfilereader as alert
from tkinter import *
from PIL import Image, ImageTk 


def findEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

path="ImageAttendence"
images=[]
classNames=[]
myList=os.listdir(path)
print(myList)

for cl in myList:
    currImg=cv2.imread(f'{path}/{cl}')
    images.append(currImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

encodeListKnown=findEncodings(images)
print("Encoding Completed !!!!!!!!!!!!!!!")
# wallpaper=cv2.imread("Resources\Wallpaper.jpg")

cap = cv2.VideoCapture(0) 
cap.set(3, 640)
cap.set(4, 480)

root = Tk() 
root.resizable(True, True)
# root.geometry("1280x720")
root.geometry("720x720")
root['background']="#c4fcfd"
root.title("Extra7")
root.bind('<Escape>', lambda e: root.quit()) 
wallpaper = PhotoImage(file="Resources\Wallpaper copy.png")
label = Label(root, image=wallpaper)
label.place(x=0, y=0)

label_widget = Label(root) 
label_widget.pack() 

tick=1

def Show_attendence():
    print("Attendece button clicked")
    os.startfile("AttendenceShow.py")
    # Start_Monitoring()
    

def Start_Monitoring():
    success, img=cap.read()
    # wallpaper[173:173+480,23:23+640]=img
    # cv2.imshow("Face Attendence",wallpaper)
    alert_Image=img
    imgS=cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS=cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    opencv_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA) 
    captured_image = Image.fromarray(opencv_image) 
    photo_image = ImageTk.PhotoImage(image=captured_image) 
    label_widget.photo_image = photo_image 
    label_widget.configure(image=photo_image) 
    label_widget.place(x=23 ,y=173)
    global tick
    tick+=1
    if(tick%100==0):
        tick/=100
        faceLocCurrFrame=face_recognition.face_locations(imgS)
        encodeCurrFrame=face_recognition.face_encodings(imgS, faceLocCurrFrame)
        for encodeFace, faceLoc in zip(encodeCurrFrame, faceLocCurrFrame):
            matches=face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDist=face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDist)
            import authorise_log as auth
            current_time = datetime.datetime.now()
            matchIndex=np.argmin(faceDist)
            if(matches[matchIndex]):
                name=classNames[matchIndex].upper()
                # print(name)
                auth.Auth(name,current_time)
                y1,x2,y2,x1=faceLoc
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0),2)
                cv2.rectangle(img, (x1,y2-35), (x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2)
            else:
                # print("Intruder")
                alert.Alert()
                cv2.imwrite('Extra7.jpeg', alert_Image)
                auth.Auth("Intruder_Alert",current_time)
                auth.Auth("ALert is triggered to the admin",current_time)
            # cv2.waitKey(50)
    # cv2.imshow("Webcam", img)
    mybutton = Button(root, text="Show Attendence", command=Show_attendence, width=15, height=2)
    mybutton.place(x=300,y=680)
    cv2.waitKey(1)
    label_widget.after(1, Start_Monitoring)
# if(mark attendence):
    # Start_Monitoring()
# def Main():
#     label_widget.photo_image = wallpaper 
#     label_widget.configure(image=wallpaper) 
#     # label_widget.place(x=23 ,y=173)
#     # print("Success")
#     label_widget.after(1, Main)
Start_Monitoring()
# Main()
root.mainloop() 