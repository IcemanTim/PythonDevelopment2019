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

        lab1 = tk.Label(text='Срок контракта :', fg='black', font='arial 15')
        lab1.place(x=250, y=90)
        scale = tk.Scale(self, length=100, orient=HORIZONTAL, from_=3, to=5,
                                  resolution=1)

        scale.place(x=380, y=90)

        def clicked():  
            label_text.configure(text="Пока ! ")  
  
        label_text = tk.Label(text="Привет ! ", font='arial 20')  
        label_text.place(x=100, y=20, width=220, height=30)  

        third_btn = Button(self, text="Печать в окно", command=clicked)  
        third_btn.place(x=350, y=20, width=220, height=30)

        def show_msg(event):
            print ("Second Button!")

        second_btn = Button(self, text=u"Печать в терминал")
        second_btn.place(x=300, y=270, width=220, height=30)
        second_btn.bind("<Button-1>",show_msg)

        # кнопка завершения
        def end_action(event):
            exit()

        first_btn = Button(self, text=u'Завершить')
        first_btn.place(x=300, y=170, width=120, height=30)
        first_btn.bind("<Button-1>", end_action)

    def center_window(self):
        width = 780
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
