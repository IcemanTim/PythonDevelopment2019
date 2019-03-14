import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

class Interface(tk.Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.gui()

    def gui(self):
        self.master.title("Testing buttons")
        self.pack(fill=BOTH, expand=True)
        self.center_window()

        # кнопка завершения
        def end_action(event):
            exit()

        q_btn = Button(self, text=u'Завершить')
        q_btn.place(x=350, y=170, width=120, height=30)
        q_btn.bind("<Button-1>", end_action)

    def center_window(self):
        width = 680
        height = 400
        screen_w = self.master.winfo_screenwidth()
        screen_h = self.master.winfo_screenheight()
        osx = (screen_w - width)/2
        osy = (screen_h - height)/2
        self.master.geometry('%dx%d+%d+%d' % (width, height, osx, osy))

def main():
    root = Tk()
    Interface(root)
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()
