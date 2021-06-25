import tkinter as tk
from tkinter import *

class Demo1:
    def __init__(self, master):
        self.master = master
        bg = PhotoImage(file='baladins.png')
    
        canvas = Canvas(master, width=400, height=400)
        canvas.pack(fill='both', expand=True)

        canvas.create_image(0,0, image=bg, anchor='nw')
        canvas.create_text(200,200, text='Etes vous pret?', font=('Helvetica', 30), fill='blue')

        openNext = Button(master, text='OUIII!!')
        openNext.bind('<Button>', lambda e: [self.new_window()])

        button1 = canvas.create_window(30, 30, anchor='nw', window=openNext)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()