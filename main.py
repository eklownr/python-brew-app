import tkinter as tk
from tkinter import ttk

# calulate vol % with OG and FG
def _alk_vol(og: float, fg: float) -> float:
    return (og - fg) * 0.132


# Window
window = tk.Tk()
window.title("Python-brew-app")
window.geometry("400x600")
bg_color = "#232323"
s = ttk.Style()
s.configure("my_color", background=bg_color)
window.configure(bg=bg_color)

# Title
tile_lable = ttk.Label(master=window, text="Calculate vol %", font="arial 26 bold", foreground="white", padding=10, background=bg_color)
tile_lable.pack()

# input fields
input_frame = ttk.Frame(master=window)
entry_og = ttk.Entry(master=input_frame, background=bg_color)
entry_fg = ttk.Entry(master=input_frame, background=bg_color) 
button = ttk.Button(master=input_frame, text="Calulate", command=_alk_vol)


entry_og.pack(pady=10)
entry_fg.pack()
button.pack(pady=20)
input_frame.pack()

# Output
output_lable = ttk.Label(master=window,  text="Output: ", font="arial 20", foreground="white", background=bg_color,padding=10)
output_lable.pack()

# run main loop
window.mainloop()

