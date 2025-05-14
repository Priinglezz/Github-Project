#here we are creating a digital clock with proper GUI

#Download Font : https://www.dafont.com/ds-digital.font
# No need to install any libraries. (t)Kinter is used for GUI in Python.
#Tkinter has another submodule that makes the widgets way cooler than the main one
#The tkinter.ttk module provides access to the Tk themed widget set, introduced in Tk 8.5
#The basic idea for tkinter.ttk is to separate, to the extent possible, the code implementing a widget’s behavior from the code implementing its appearance.
#To override the basic Tk widgets, the import should follow the Tk import given below. That code causes several tkinter.ttk widgets (Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale and Scrollbar) to automatically replace the Tk widgets.


# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')

# This function is used to
# display time on the label
def time():
   string = strftime('%H:%M:%S %p')
#For clock formats  12hrs, change the strftime('%H:%M:%S %p') to
#strftime('%I:%M:%S %p').
#1000 implies refresh the clock every 1000 milisecond.
   lbl.config(text = string)
   lbl.after(1000, time)

# Styling the label widget so that clock
# will look more attractive
#We downloaded ds-digital font from the link below:
#https://www.dafont.com/ds-digital.font
lbl = Label(root, font = ('ds-digital', 80),
         background = 'purple',
         foreground = 'white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
time()

mainloop()


