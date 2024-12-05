#Import Tkinter, i use it in college so i know a bit of how to use it.
import tkinter as tk

# Create a Main Application Window.
root = tk.Tk() 
root.title("My Desktop Application")
label = tk.Label(root, text="Hello, World!") 
label.pack()  
button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked!")) 
button.pack()
root.mainloop()