# 📦 Import required libraries
import gspread  # Allows Python to read/write Google Sheets
import pandas as pd  # For handling structured data (tables)
import tkinter as tk  # For creating the graphical user interface
from tkinter import scrolledtext, Entry, Button  # Specific widgets from tkinter
from oauth2client.service_account import ServiceAccountCredentials  # For Google authentication
from fuzzywuzzy import process  # For matching user input to similar text in your FAQ

# Step 1: Set up Google Sheets authentication
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]  # Required API access scopes
CREDS = ServiceAccountCredentials.from_json_keyfile_name("keys.json", SCOPE)  # Load credentials from keys.json
client = gspread.authorize(CREDS)  # Authorize access to Google Sheets using the credentials

# Step 2: Open the specific Google Sheet
spreadsheet = client.open("chatbot")  # Open a spreadsheet named 'chatbot'
sheet = spreadsheet.worksheet("Sheet1")  # Access the first worksheet named 'Sheet1'

# Step 3: Load the Google Sheet data into a pandas DataFrame
faq_df = pd.DataFrame(sheet.get_all_records())  # Get all rows as dictionaries and convert to a DataFrame


# Step 4: Define the chatbot logic
#user_input is the name of our entrybox we have created towards the end of this code
def chatbot_response(user_input):
    """Find the best-matching answer from the FAQ database."""

    # Use fuzzy matching to find the most similar question from the FAQ
    #finds/extracts the closest match between the user's input and those FAQ questions
    match = process.extractOne(user_input, faq_df["Question"])

    # If there's no match or it's invalid, return a default message
    if not match or len(match) < 2:
        return "🤖 Sorry, I couldn't find an answer for that. Try rephrasing!"

    best_match, confidence = match[:2]  # Extract matched question and its confidence score

    # Explaining our code above:
    # We are using fuzzywuzzy library to compare the user's message with your list of questions, and the confidence level.
    # The MATCH brings QUESTIONS and CONFIDENCE. It returns something like this: match = ("What is your return policy?", 87)
    # len(match) < 2: this line makes sure the tuple has both elements: the matched question and the confidence score (int from 0 to 100).

    best_match, confidence = match[:2]  # "Take the first two items from the match result, and assign them to two variables: best_match and confidence."

    # If the confidence is above a threshold, return the corresponding answer
    if confidence > 60:
        answer = faq_df.loc[faq_df["Question"] == best_match, "Answer"].values  # Look up the answer in the DataFrame
        return answer[0] if len(answer) > 0 else "🤖 No answer available."
    else:
        return "🤖 Sorry, I couldn't find an answer for that."


# ✅ Step 5: Define what happens when the user clicks "Send"
def send_message():
    """Handle user input and display the chatbot response."""

    user_text = user_input.get()  # Get the text the user entered

    if user_text.strip():  # If the input is not just empty spaces
        chat_display.insert(tk.END, f"👤 You: {user_text}\n", "user")  # Display user's message in blue
        response = chatbot_response(user_text)  # Get the chatbot's response
        chat_display.insert(tk.END, f"🤖 Chatbot: {response}\n\n", "bot")  # Display chatbot's response in green
        chat_display.yview(tk.END)  # Scroll to the bottom to show the latest message

    user_input.delete(0, tk.END)  # Clear the input field


# ✅ Step 6: Set up the Tkinter GUI
root = tk.Tk()  # Create the main window
root.title("Chatbot Assistant")  # Set the window title
root.geometry("500x500")  # Set the window size

# ✅ Create the chat display area with scrolling
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50)  # Chat window
chat_display.pack(pady=10)  # Add some vertical padding
chat_display.tag_config("user", foreground="blue")  # Style for user messages
chat_display.tag_config("bot", foreground="green")  # Style for bot responses

# ✅ Create the input field where users type their questions
user_input = Entry(root, width=33, justify=tk.CENTER, font=('courier', 14, 'bold'))  # Entry widget for user input
user_input.pack(pady=5)

# ✅ Create the "Send" button and connect it to send_message()
send_button = Button(root, text="Send", command=send_message)  # Button to trigger response
send_button.pack()

# ✅ Start the main loop to display the GUI and wait for user interaction
root.mainloop()
