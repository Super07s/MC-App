import tkinter as tk
from tkinter import messagebox

# Function to validate pin and open the atm window
def validate_and_open_atm():
    pin = entry.get()
    if len(pin) == 4 and pin.isdigit():
        open_atm_window()
    else:
        messagebox.showerror("Invalid PIN", "Please enter a 4-digit PIN.")

# Function to open the atm-style window
def open_atm_window():
    atm_window = tk.Toplevel(root)
    atm_window.title("ATM Interface")
    atm_window.geometry("300x400")
    
screen = tk.Label(atm_window, text="Welcome!\nSelect an Option", 
                       bg="black", fg="green", font=("Courier", 14), 
                       height=4, width=30)
screen.pack(pady=10)
    
# button labels for second window
button_labels = ["Balance", "Deposit", "Withdraw", "Transfer", "Help", "Exit"]

button_frame = tk.Frame(atm_window)
button_frame.pack(pady=10)

#i didnt know how to do this part so i google it, and i think it worked
for i, label in enumerate(button_labels):
        button = tk.Button(button_frame, text=label, width=12, height=2, 
                           command=lambda lbl=label: button_action(lbl))
        button.grid(row=i//3, column=i%3, padx=10, pady=10)    

#action button to click

def button_action(option):
    if option == "Exit":
        root.quit()
    else:
        messagebox.showinfo("Action", f"You selected: {option}")

root = tk.Tk()
root.title("Atm Login")
root.geometry("300x150")


tk.Label(root, text="Enter 4-digit PIN:").pack(pady=5)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)

#submit button and the app run
tk.Button(root, text="Enter", command=validate_and_open_atm).pack(pady=10)
root.mainloop()