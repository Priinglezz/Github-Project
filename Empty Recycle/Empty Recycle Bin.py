#Emptying Recycle Bin:
# Import the 'winshell' library, which provides functions to interact with the Windows shell, including Recycle Bin operations
import winshell

try:
    # Call the 'recycle_bin()' method from the winshell library, which accesses the Recycle Bin
    # The 'empty' method is then called to empty the Recycle Bin with the following arguments:
    # - 'confirm=False': This disables the confirmation prompt, so it empties the Recycle Bin without asking for confirmation
    # - 'show_progress=False': This prevents showing a progress bar while the Recycle Bin is emptied
    # - 'sound=True': This plays a sound when the Recycle Bin is emptied
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)

    # If the operation is successful, print this message to the console
    print("Recycle bin is emptied Now")
except:
    # If an error occurs (e.g., the Recycle Bin is already empty), print this message
    print("Recycle bin already empty")
