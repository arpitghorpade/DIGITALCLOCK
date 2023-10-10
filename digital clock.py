import tkinter as tk
from time import strftime

def time_update():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time_update)

root = tk.Tk()
root.title('Digital Clock')
root.geometry('400x200')
root.resizable(False, False)

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center', pady=20)

time_update()

root.mainloop()
