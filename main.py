import tkinter as tk
import ttkbootstrap as ttk

# calulate vol % with OG and FG
def _alk_vol():
    og = entry_og_int.get()
    fg = entry_fg_int.get()
    result: float = (og - fg) * 0.132
    round_result = round(result, 2)
    output_string.set(str(round_result) + " Vol %")


# Window
window = ttk.Window(themename="cyborg")
window.title("Python-brew-app")
window.geometry("500x600")

# Title
tile_lable = ttk.Label(master=window, text="Calculate vol %", font="arial 26 bold", foreground="white", padding=10)
tile_lable.pack()

# input fields
input_frame = ttk.Frame(master=window)
entry_og_int = tk.IntVar()
entry_fg_int = tk.IntVar()
og_lable = ttk.Label(master=input_frame, text="OG: ")
entry_og = ttk.Entry(master=input_frame, textvariable=entry_og_int)
fg_lable = ttk.Label(master=input_frame, text="FG: ")
entry_fg = ttk.Entry(master=input_frame, textvariable=entry_fg_int) 
button = ttk.Button(master=input_frame, text="Calulate", command=_alk_vol)

og_lable.pack()
entry_og.pack(pady=20)
fg_lable.pack()
entry_fg.pack(pady=20)

button.pack(pady=20)
input_frame.pack()

# Output
output_string = tk.StringVar()
output_lable = ttk.Label(
    master=window,  
    text="Output: ", 
    font="arial 20", 
    foreground="white", 
    padding=10,
    textvariable=output_string)
output_lable.pack()

# run main loop
window.mainloop()

