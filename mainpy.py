import tkinter as tk
import pyttsx3
from tkinter import messagebox
import alphaToBraille, brailleToAlpha


#Code for text to braille conversion
def convert_text():
    text = text_entry.get("1.0", "end-1c")
    filename = filename_entry.get()
    braille = alphaToBraille.translate(text)
    save_as_braille(braille, filename)


def save_as_braille(braille, filename):
    file = open(filename + ".txt", "w", encoding="utf-8")
    file.write(braille)
    messagebox.showinfo("Saved", "Successfuly Converted to Braille and Saved")


def search_file():
    filename = search_entry.get()
    try:
        file = open(filename + ".txt", "r", encoding="utf-8") 
        content = file.read()
        text_widget.delete("1.0", "end")  # Clear existing content
        text_widget.insert("1.0", content)  # Insert file content into the text widget
        # print(content)  # printing in the cmd line  
    except FileNotFoundError:
        messagebox.showerror("Error","File not found!!")
        # print("File not found!") #print in cmd line

# ------

#Code for braille to text conversion
def convert_text2():
    text = text_entry2.get("1.0", "end-1c")
    filename = filename_entry2.get()
    text1 = brailleToAlpha.translate(text)
    save_as_text(text1, filename)


def save_as_text(text, filename):
    file = open(filename + ".txt", "w", encoding="utf-8")
    file.write(text)
    messagebox.showinfo("Saved", "Successfuly Converted to Text and Saved")


def search_file2():
    filename = search_entry2.get()
    try:
        with open(filename + ".txt", "r", encoding="utf-8") as file:
            content = file.read()
            text_widget2.delete("1.0", "end")  # Clear existing content
            text_widget2.insert("1.0", content)  # Insert file content into the text widget
            # print(content)  # display the content in cmd line
    except FileNotFoundError:
        messagebox.showerror("Error","File not found!!")
        # print("File not found!") #print in cmd line

# -----

# Function to read text from a file
def convert_to_speech_from_file():
    try:
       file_path = search_entry2.get()+".txt"
       if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait() 
    except FileNotFoundError:
        messagebox.showerror("Warning","Enter Filename!!")

#-------

# Function to read text from message box
def convert_to_speech_from_messagebox():
    text = text_entry.get("1.0", "end-1c")
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

#------

# Create the main window
window = tk.Tk()

# Set the background color
window.configure(background='light pink')

# Configure the columns to have equal weight and size
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

window.title("Text to Braille & Braille to Text Converter")

# Text-to-Braille converter 
heading_label = tk.Label(window, text="Text-to-Braille Converter", font=("Helvetica", 16, "bold"), background="light grey")
heading_label.grid(row=0, column=0, pady=10)

# Create the text entry and label for 'Convert Text'
text_label = tk.Label(window, text="Enter Text:")
text_label.grid(row=1,column=0, padx=10, pady=[2,2])
text_entry = tk.Text(window, height=10, width=90)
text_entry.grid(row=2, column=0, padx=10, pady=[2,10])

# Create the filename entry and label for 'Convert Text'
filename_label = tk.Label(window, text="Enter Filename:")
filename_label.grid(row=3, column=0, padx=10, pady=[10,2])
filename_entry = tk.Entry(window)
filename_entry.grid(row=4, column=0, padx=10, pady=[2,2])

# Create the 'Convert Text' button
convert_button = tk.Button(window, text="Convert Text to Braille", command=convert_text, foreground="white", background="brown")
convert_button.grid(row=5, column=0, padx=10, pady=[2,10])

#create button to convert text to speech directly
btn_convert = tk.Button(window, text="Convert Text to Speech", command=convert_to_speech_from_messagebox, foreground="white", background="blue")
btn_convert.grid(row=6, column=0,padx=10,pady=10)

# Create the search entry and label
search_label = tk.Label(window, text="Search for Braille file:")
search_label.grid(row=7, column=0, padx=10, pady=[10,2])
search_entry = tk.Entry(window)
search_entry.grid(row=8, column=0, padx=10, pady=[2,2])

# Create the 'Search' button
search_button = tk.Button(window, text="Search", command=search_file, foreground="white", background="dark green")
search_button.grid(row=9, column=0, padx=10, pady=[2,10])

# Create output label 
output_label = tk.Label(window, text="Content of Braille file:")
output_label.grid(row=10, column=0, padx=10, pady=[10,2])

# Create the text widget to show the file content
text_widget = tk.Text(window, height=10, width=90)
text_widget.grid(row=11, column=0, padx=10, pady=[2,10])

# ------

# Braille-to-Text converter
heading_label = tk.Label(window, text="Braille-to-Text Converter", font=("Helvetica", 16, "bold"), background="light grey")
heading_label.grid(row=0, column=1, pady=10)

# Create the text entry and label for 'Convert Braille'
text_label2 = tk.Label(window, text="Enter Braille:")
text_label2.grid(row=1, column=1, padx=10, pady=[2,2])
text_entry2 = tk.Text(window, height=10, width=90)
text_entry2.grid(row=2, column=1, padx=10, pady=[2,10])

# Create the filename entry and label for 'Convert Braille'
filename_label2 = tk.Label(window, text="Enter Filename:")
filename_label2.grid(row=3, column=1, padx=10, pady=[10,2])
filename_entry2 = tk.Entry(window)
filename_entry2.grid(row=4, column=1, padx=10, pady=[2,2])

# Create the 'Convert Braille' button
convert_button2 = tk.Button(window, text="Convert Braille to Text", command=convert_text2, foreground="white", background="brown")
convert_button2.grid(row=5, column=1, padx=10, pady=[2,10])

#create button to read a text file
btn_select_file = tk.Button(window, text="Read Text from File", command=convert_to_speech_from_file, foreground="white", background="blue")
btn_select_file.grid(row=6, column=1,padx=10, pady=10)

# Create the search entry and label
search_label = tk.Label(window, text="Search for Text file:")
search_label.grid(row=7, column=1, padx=10, pady=[10,2])
search_entry2 = tk.Entry(window)
search_entry2.grid(row=8, column=1, padx=10, pady=[2,2])

# Create the 'Search' button
search_button = tk.Button(window, text="Search", command=search_file2, foreground="white", background="dark green")
search_button.grid(row=9, column=1, padx=10, pady=[2,10])

# Create output label2 
output_label2 = tk.Label(window, text="Content of the Text file:")
output_label2.grid(row=10, column=1, padx=10, pady=[10,2])

# Create the text widget to show the file content
text_widget2 = tk.Text(window, height=10, width=90)
text_widget2.grid(row=11, column=1, padx=10, pady=[2,10])

# Start the Tkinter event loop
window.mainloop()
