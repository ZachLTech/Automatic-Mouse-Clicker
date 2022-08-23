from ast import Delete
from cProfile import label
from tkinter import font
from turtle import bgcolor
import pyautogui
import pytesseract
import PIL
from PIL import ImageTk
from PIL import Image
import time
import random
import keyboard
import tkinter as tk
from tkinter import END, Image, filedialog, Text
import os
import shutil
import cv2
import sys

#500,200 = mid

#Where our selected images are stored while program is being used
Images = []


#Makes window
root = tk.Tk()

root.geometry('1000x500')

#makes a canvas
canvas = tk.Canvas(root, height=500, width=1000, bg="#080934")
#020C17
#263D42
root.iconbitmap("Crystal_Project_Mouse.ico")

#frame for button1
frame = tk.Frame(canvas, bg="white")
frame.place(width=150, height=50, relx=0.076, rely=0.1)
#frame for button2
frame2 = tk.Frame(canvas, bg="white")
frame2.place(width=150, height=50, relx=0.076, rely=0.3)
#frame for image file labels
frame3 = tk.Frame(canvas, bg="gray")
frame3.place(width=670, height=30, relx=0.16, rely=0.7)
#Frame for button 3
frame4 = tk.Frame(canvas, bg="white")
frame4.place(width=150, height=50, relx=0.076, rely=0.5)
#frame for label
frame5 = tk.Frame(canvas, bg="#080934")
frame5.place(width=250, height=70, relx=0.7, rely=0.15)
#frame for clear image button
frame6 = tk.Frame(canvas, bg="white")
frame6.place(width=150, height=40, relx=0.75, rely=0.5)
#howtouse button
frame7 = tk.Frame(canvas, bg="white")
frame7.place(width=150, height=40, relx=0.41, rely=0.84)
#mouse image
frame8 = tk.Frame(canvas, bg="black")
frame8.place(width=200, height=260, relx=0.39, rely=0.12)
#clickspeedlabel
frame9 = tk.Frame(canvas, bg="#080934")
frame9.place(width=350, height=50, relx=0.58, rely=0.78)

picforfrontpage = ImageTk.PhotoImage(file="Crystal_Project_Mouse.png")
labelforfrontpage= tk.Label(frame8, image = picforfrontpage, bg='#080934')
labelforfrontpage.pack()

#function for insert image button
def ImageInsert():
    for widget in frame3.winfo_children():
        widget.destroy()
    filename= filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("images","*.png"), ("all files", "*.*")))
    Images.append(filename)
    print(filename)
    for app in Images:
        imagefilename = tk.Label(frame3, text=app, bg="gray")
        imagefilename.pack()
#insert image button
InsertImage = tk.Button(frame, text="Insert Image", padx=100, pady=100, fg="white", bg="black", command=ImageInsert)
InsertImage.pack()

#directions button function
def Howtouse():
    root2 = tk.Toplevel()
    root2.title('How To Use')
    #program_directory=sys.path[0]
    #root.iconphoto(True, tk.PhotoImage(file=os.path.join(program_directory, "simple-question-mark-icon-29.PNG")))
    root2.iconbitmap('simple-question-mark-icon-29.ico')
    canvashowtouse = tk.Canvas(root2, height=1067, width=620, bg="#696969")
    framehowtouse = tk.Frame(canvashowtouse, bg="white")
    framehowtouse.place(width=620, height=1067, relx=0, rely=0)
    picforinstructions = ImageTk.PhotoImage(file="actuallygoodsize.PNG")
    labelforinstructions= tk.Label(framehowtouse, image = picforinstructions)
    labelforinstructions.pack()
    canvashowtouse.pack()
    root2.mainloop()




#text box for clicking speed
entry4clickingspeed = tk.Entry(canvas) 
canvas.create_window(750, 450, window=entry4clickingspeed)

#label for text entry
TBoxLabel4clickspeed = tk.Label(frame9, text="Time Between Clicks (Seconds)", bg='#080934', fg='white')
TBoxLabel4clickspeed.pack()  


#directions button
directionsbutton = tk.Button(frame7, text="How To Use", padx=100, pady=100, fg="white", bg="black", command=Howtouse)
directionsbutton.pack()

#text entry box
entry1 = tk.Entry(canvas) 
canvas.create_window(824, 195, window=entry1)

 #label for text entry
TBoxLabel = tk.Label(frame5, text="Detection Accuracy %\n(Decimal Form Only)", bg="#080934", fg="white")
TBoxLabel.pack()   

#function for clear image button
def ClearImage():
    for widget in frame3.winfo_children():
        os.remove('copyofselectedimg.PNG')
        widget.destroy()
        Images.clear()
#ClearImage Button
ImageClear = tk.Button(frame6, text="Clear Image", padx=100, pady=100, fg="white", bg="black", command=ClearImage)
ImageClear.pack()

#function for start clicing button 
def Clickstart():
    imagestr = ''.join(Images)
    copiedimgindir = shutil.copyfile(imagestr, 'copyofselectedimg.PNG')
    enteredpercent = entry1.get()
    if enteredpercent == (f'0.1') or (f'0.2'):
        locationofimages = pyautogui.locateOnScreen('copyofselectedimg.PNG', grayscale=False, confidence=enteredpercent)
        print(locationofimages)
        if locationofimages != None:
            enteredspeed = entry4clickingspeed.get()
            speedint = int(enteredspeed)
            pyautogui.moveTo(locationofimages)
            time.sleep(speedint)
            pyautogui.click()
            print('test')
        root.after(700, Clickstart)
    else:
        print('.')


#start clicking button (function not yet made)
StartClicking = tk.Button(frame2, text="Start Clicking!", padx=100, pady=100, fg="white", bg="black", command=Clickstart)
StartClicking.pack()

#function for stop clicking button
def Clickstop():
    entry1.delete(0, END)
#stop clicking button
StopClicking = tk.Button(frame4, text="Stop Clicking!", bg="black", fg="white", padx=100, pady=100, command=Clickstop)
StopClicking.pack()



root.title('Image Clicker')

#runs canvas
canvas.pack()
#runs window
root.mainloop()


#add clicking speed