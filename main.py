from tkinter import *
import tkinter.font as font
from subprocess import call
import sys

root = Tk()
root.title('Merge Sort Representation')
root.iconbitmap('D:/pyproject/MergeSortVisualization/img/logo.ico')
root.geometry('1200x675')

# Background Image
bg_set = Canvas(root, bg="gray16", height=200, width=200)
filename = PhotoImage(file="D:/pyproject/MergeSortVisualization/img/sort.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Button For the Next Screen
def clickbutton():
    call(["python", "sortingui.py"])
    root.destroy()


buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
myButton = Button(root, text="START SORTING", command=clickbutton, fg="blue", bg="red", pady=10, padx=10,
                  font=buttonFont)
myButton.place(x=800, y=600)

bg_set.pack()

root.mainloop()
