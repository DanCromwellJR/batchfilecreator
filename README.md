# batchfilecreator
for each line in a text file, it will create a blank file in the requested format. useful for making text files of task lists

# Create Multiple Files

This Python program provides a simple graphical user interface (GUI) to create multiple files based on the lines of a text file. The input file should contain one file name per line. The program will create a new file for each line in the text file, using the specified file extension.

## Requirements

- Python 3.x
- tkinter

## Usage

1. Run the Python script `python create_multiple_files.py`.
2. Click on the "Select file" button to choose the input text file containing the file names.
3. Click on the "Select folder" button to choose the output folder where the new files will be created.
4. Enter the desired file extension for the new files in the "File extension" entry box.
5. Click on the "Go" button to create the new files.

Once the new files have been created, a "Files created successfully." message will appear.

## Example

Suppose you have an input file called `input.txt` containing the following content:

```
file1
file2
file3
```

After selecting the input file, output folder, and specifying the file extension as "txt", the program will create the following files in the output folder:

- file1.txt
- file2.txt
- file3.txt

Each of these files will contain the same content as their respective file name (e.g., file1.txt will contain "file1").

## Troubleshooting

- Make sure you have Python 3.x installed and tkinter is available in your Python environment.
- Ensure that the input file path and output folder path are valid.
- Check if you have write permission to the selected output folder.
