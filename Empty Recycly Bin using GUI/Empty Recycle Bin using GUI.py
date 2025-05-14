#Empty Reyclce Bin Using GUI

import tkinter as tk  # Import Tkinter for GUI
from tkinter import messagebox  # Import messagebox for displaying alerts
import winshell  # Import winshell for Recycle Bin operations


# Function to empty the Recycle Bin
def empty_recycle_bin():
    try:
        # Access the Recycle Bin and empty it with specific options
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)

        # If the operation is successful, show a success message
        messagebox.showinfo("Success", "Recycle bin is emptied now.")  # Display success message
    except Exception as e:
        # If an error occurs (e.g., the Recycle Bin is already empty), show an error message
        messagebox.showerror("Error", "Recycle bin is already empty.")  # Display error message


# Create the main window (GUI window)
root = tk.Tk()  # Create a Tkinter window
root.title("Recycle Bin Emptying Tool")  # Set the title of the window
root.geometry("300x150")  # Set the size of the window

# Create a button to empty the Recycle Bin
empty_button = tk.Button(root, text="Empty Recycle Bin", command=empty_recycle_bin)  # Create the button
empty_button.place(x=100, y=50)
#empty_button.pack(pady=20)  # alternative ways of writing the code above

# Start the Tkinter event loop (this keeps the window open)
root.mainloop()
