import tkinter as tk
from tkinter import filedialog
import os

# Define a function to create a new file for each line in a text file
def create_files():
    # Get the input file path and extension from the GUI
    input_path = input_file_path.get()
    extension = file_extension.get()
    
    # Get the output folder path from the GUI
    output_folder_path = output_folder_path_var.get()
    
    # Open the input file for reading
    with open(input_path, "r") as input_file:
        for line in input_file:
            # Remove any newline characters from the line
            line = line.strip()
            
            # Create a new file with the name of the line and the given extension
            file_name = f"{line}.{extension}"
            file_path = os.path.join(output_folder_path, file_name)
            with open(file_path, "w") as new_file:
                # Write the line content to the new file
                new_file.write(line)
    
    # Display a message when the files have been created
    output_label.config(text="Files created successfully.")

# Define a function to select the input file
def select_input_file():
    input_path = filedialog.askopenfilename()
    input_file_path.set(input_path)

# Define a function to select the output folder
def select_output_folder():
    output_folder_path = filedialog.askdirectory()
    output_folder_path_var.set(output_folder_path)

# Create a GUI window
window = tk.Tk()
window.title("Create Multiple Files")

# Create a label and button for selecting the input file
input_file_path = tk.StringVar()
input_label = tk.Label(window, text="Input file:")
input_label.grid(row=0, column=0)
input_path_label = tk.Label(window, textvariable=input_file_path)
input_path_label.grid(row=0, column=1)
input_button = tk.Button(window, text="Select file", command=select_input_file)
input_button.grid(row=0, column=2)

# Create a label and button for selecting the output folder
output_folder_path_var = tk.StringVar()
output_label = tk.Label(window, text="Output folder:")
output_label.grid(row=1, column=0)
output_path_label = tk.Label(window, textvariable=output_folder_path_var)
output_path_label.grid(row=1, column=1)
output_button = tk.Button(window, text="Select folder", command=select_output_folder)
output_button.grid(row=1, column=2)

# Create a label and entry box for the file extension
file_extension = tk.StringVar()
extension_label = tk.Label(window, text="File extension:")
extension_label.grid(row=2, column=0)
extension_entry = tk.Entry(window, textvariable=file_extension)
extension_entry.grid(row=2, column=1)

# Create a button to create the files
create_button = tk.Button(window, text="Go", command=create_files)
create_button.grid(row=3, column=1)

# Run the GUI window
window.mainloop()
