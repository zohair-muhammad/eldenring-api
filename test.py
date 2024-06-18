import tkinter as tk
from tkinter import ttk

app=tk.Tk()
app_FRAME=tk.Frame(app,relief=tk.GROOVE)
app_FRAME.pack()


def clicked_on_arrow():
    print("see the list")

def var_changed():
    print("var changed")

_list = ["a","b","c"]
_var = tk.StringVar()
_var.trace("w", lambda name, index, mode, x=_var: var_changed())

_COMBOBOX = ttk.Combobox(app_FRAME, postcommand=clicked_on_arrow(), values=_list, textvariable=_var)
_COMBOBOX.pack()
random_BUTTON = tk.Button(app_FRAME, text="the list can overlap over me !")
random_BUTTON.pack(fill=tk.BOTH, expand=True)

app.mainloop()