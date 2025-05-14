#This GUI app allows us to calculate age of people
#when they input date of birth
from tkinter import *
import datetime
root = Tk()
root.geometry("400x180")
root.title("Age Calculator")
def calculateage():
    birthdate = datetime.datetime(int(YearVariable.get()), int(MonthVariable.get()), int(DayVariable.get()))
    age = datetime.datetime.now() - birthdate
    convertdays = int(age.days)
    ageyears = round(convertdays/365, 2)
    Label(text =f"{NameVariable.get()} your age is {ageyears}").grid(row=6, column=1)
lb1 = Label(root, text = "Your Name" ).grid(row=1, column=1, padx=90)
lb2 = Label(root, text = "Year" ).grid(row=2, column=1, padx=90)
lb3 = Label(root, text = "Month").grid(row=3, column=1, padx=90)
lb4 = Label(root, text = "Day" ).grid(row=4, column=1, padx=90)
NameVariable = StringVar()
YearVariable = StringVar()
MonthVariable = StringVar()
DayVariable = StringVar()
EntryName = Entry(root, textvariable= NameVariable).grid(row=1, column=2)
EntryYear = Entry(root, textvariable= YearVariable).grid(row=2, column=2)
EntryMonth = Entry(root, textvariable= MonthVariable).grid(row=3, column=2)
EntryDay = Entry(root, textvariable= DayVariable).grid(row=4, column=2)
button1 = Button(root, text="Submit", command = calculateage)
button1.grid(row=5, column=1)
root.mainloop()