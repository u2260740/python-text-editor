# Import the Tkinter library used for the GUI
import tkinter as tk
# Import the filedialog module from Tkinter
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        # Initialize the root window
        self.root = root
        # Set the title of the window
        self.root.title("Text Editor")
        # Create a text widget for the text input
        self.text_area = tk.Text(self.root, wrap="word")
        # Pack the text to fill the window
        self.text_area.pack(expand=True, fill="both")

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)

        # Create a file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        # Add an "Open" file option to the menu dropdown
        self.file_menu.add_command(label="Open", command=self.open_file)
        # Add a "Save" file option to the menu dropdown
        self.file_menu.add_command(label="Save", command=self.save_file)
        # Adds a separator in the dropdown
        self.file_menu.add_separator()
        # Add an "Exit" option to the dropdown
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        # Create the cascading/dropdown menu button and add to the menu bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Configure the window with the menu bar
        self.root.config(menu=self.menu_bar)


    # Open file function
    def open_file(self):
        # Open file dialog to select the file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        # Check if a file is selected
        if file_path:
            with open(file_path, "r") as file:
                # Delete the current text in the text area
                self.text_area.delete(1.0, tk.END)
                # Insert the content into the text area
                self.text_area.insert(tk.END, file.read())

    # Save file function
    def save_file(self):
        # Open file dialog to save file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        # Check if a file path was provided
        if file_path:
            with open(file_path, "w") as file:
                # Write contents of the text area to the file
                file.write(self.text_area.get(1.0, tk.END))

def main():
    # Create a tkinter root window
    root = tk.Tk()
    # Create an instance of the TextEditor class
    editor = TextEditor(root)
    # Makes the window not close unless the user closes it
    root.mainloop()

# Ensures it doesn't run unless the user runs it directly
if __name__ == "__main__":
    main()