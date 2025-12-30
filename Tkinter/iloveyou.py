import tkinter as tk
import random
from tkinter import messagebox

# --- Configuration & Colors (NiceUI Theme) ---
COLOR_BG = "#2C3E50"        # Dark Blue-Grey
COLOR_TEXT = "#ECF0F1"      # Off-White
COLOR_YES = "#27AE60"       # Emerald Green
COLOR_YES_HOVER = "#2ECC71" # Lighter Green
COLOR_NO = "#E74C3C"        # Alizarin Red
COLOR_NO_HOVER = "#FF6B6B"  # Lighter Red
FONT_MAIN = ("Verdana", 16, "bold")
FONT_BTN = ("Verdana", 12, "bold")

def move_button(event):
    # Ensure we get the current valid width/height
    current_width = window.winfo_width()
    current_height = window.winfo_height()
    
    # Calculate safe boundaries
    button_w = no_button.winfo_width() or 60
    button_h = no_button.winfo_height() or 35
    
    max_x = current_width - button_w - 20
    max_y = current_height - button_h - 20

    # Safety check to prevent negative range
    if max_x > 0 and max_y > 0:
        new_x = random.randint(20, max_x)
        new_y = random.randint(20, max_y)
        no_button.place(x=new_x, y=new_y)

def accepted():
    messagebox.showinfo("Success", "I knew you liked me! ❤️")
    window.destroy()

# --- Setup Main Window ---
window = tk.Tk()
window.title("Proposal")

# 1. Define size
window_width = 450
window_height = 450
window.configure(bg=COLOR_BG)

# 2. Remove Title Bar
window.overrideredirect(True) 

# 3. Center the window
window.update_idletasks() 
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_c = int((screen_width / 2) - (window_width / 2))
y_c = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x_c}+{y_c}")

# --- UI Styling Elements ---

# Border Frame
border = tk.Frame(window, bg=COLOR_TEXT)
border.place(x=0, y=0, width=window_width, height=window_height)

# Main Inner Canvas
main_frame = tk.Frame(window, bg=COLOR_BG)
main_frame.place(x=2, y=2, width=window_width-4, height=window_height-4)

# --- Widgets ---
label = tk.Label(main_frame, text="I like You,\nDo You Like Me?", 
                 font=FONT_MAIN, bg=COLOR_BG, fg=COLOR_TEXT, justify="center")
label.pack(pady=(100, 50)) 

# Yes Button
yes_button = tk.Button(main_frame, text="Yes", font=FONT_BTN, 
                       bg=COLOR_YES, fg="white", activebackground=COLOR_YES_HOVER, activeforeground="white",
                       bd=0, highlightthickness=0, relief="flat",
                       cursor="hand2", width=10, height=2,
                       command=accepted)
yes_button.place(x=(window_width//2) - 55, y=220) 

# No Button
no_button = tk.Button(main_frame, text="No", font=FONT_BTN, 
                      bg=COLOR_NO, fg="white", activebackground=COLOR_NO_HOVER, activeforeground="white",
                      bd=0, highlightthickness=0, relief="flat",
                      cursor="hand2", width=10, height=2)
no_button.place(x=(window_width//2) - 55, y=290) 

# --- Bindings ---
no_button.bind("<Enter>", move_button) 

window.mainloop()