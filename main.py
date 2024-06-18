import json
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import customtkinter


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(500,500)
        self.title("Elden Ring Search")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name, name=""):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Elden Ring Search", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Weapons",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Sorceries",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Incantations",
                            command=lambda: controller.show_frame("PageThree"))

        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Weapons", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        _list = []
        data_file = open('api/public/data/weapons.json')
        data = json.load(data_file)

        for key in data:
            for v in key:
                if v =='name':
                    _list.append(key[v])

        _var = tk.StringVar()
        _COMBOBOX = ttk.Combobox(self, values=_list, textvariable=_var)
        _COMBOBOX.pack()

        def on_select(event):
            global weapon_name
            weapon_name = ""
            weapon_name = _var.get()


        _COMBOBOX.bind("<<ComboboxSelected>>", on_select)

        def open_weapon_page():
            global weapon_name
            newWindow = tk.Toplevel(self)

            # sets the title of the
            # Toplevel widget
            newWindow.title(weapon_name)

            # sets the geometry of toplevel
            newWindow.geometry("500x500")

            # A Label widget to show in toplevel
            label = tk.Label(newWindow, text=weapon_name, font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)
            d = ""

            for key in data:
                for v in key:
                    if v == 'name' and key[v] == weapon_name:
                        d = key['description']

            desc = tk.Label(newWindow, text = d, wraplength=500, justify="center")
            desc.pack()
        sbutton = tk.Button(self, text="Submit",
                           command = open_weapon_page)

        sbutton.pack()

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        data_file.close()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()