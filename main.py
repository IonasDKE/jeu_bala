import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.template(self.master)
        self.mainMenu()
        
    def mainMenu(self):
        self.master.title('Jeu Baladins')

        label = Label(self.master, text='Etes vous pret?')
        label.pack(side='top')

        openNext = tk.Button(self.master, text='OUIII!!')
        openNext.bind('<Button>', lambda e: [self.start()])
        openNext.pack()

        quit = tk.Button(self.master, text="QUIT", command=self.master.destroy)
        quit.pack()
    

    def start(self):
        self.master.withdraw()
        newWind = Toplevel(self.master)
        newWind.protocol("WM_DELETE_WINDOW", self.master.destroy)
        newWind.geometry("275x400")

        space3 = Label(newWind, text='')
        space3.pack(side='top')
        label = Label(newWind, text='Question 1:')
        label.pack(side='top')
        space1 = Label(newWind, text='')
        space1.pack(side='top')
        question = Label(newWind, text='Quel est la couleur des chemises pioniers?')
        question.pack(side='top')
        space2 = Label(newWind, text='')
        space2.pack(side='top')
        
        ans1 = tk.Button(newWind, text='blue claire')
        ans1.bind('<Button>', lambda e: [popup()])
        ans1.pack(side='top')
        ans2 = tk.Button(newWind, text='vert')
        ans2.bind('<Button>', lambda e: [popup()])

        ans2.pack(side='top')
        ans3 = tk.Button(newWind, text='bleu fonce')
        ans3.bind('<Button>', lambda e: [popup()])

        ans3.pack(side='top')
        ans4 = tk.Button(newWind, text='rouge')
        ans4.bind('<Button>', lambda e: [popupGood(), newWind.withdraw(), self.q2()])

        ans4.pack(side='top')

    def q2(self):
        newWind = Toplevel(self.master)
        newWind.protocol("WM_DELETE_WINDOW", self.master.destroy)
        newWind.geometry("275x400")

        space1 = Label(newWind, text='')
        space1.pack(side='top')


    def template(self, window):

        windowWidth = window.winfo_reqwidth()
        windowHeight = window.winfo_reqheight()
        
        positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2) 
        positionDown = int(window.winfo_screenheight()/2 - windowHeight/2) -80
        
        window.geometry("+{}+{}".format(positionRight, positionDown))
        window.title("Scout BDV")


# Informe qu'une contrainte a bien ete ajoutée
def popup():
    showinfo(message="Mauvasie reponse! Reviens plus tard")

def popupGood():
    showinfo(message="BIEN JOUE!")

def main():
    master = tk.Tk()
    master.protocol("WM_DELETE_WINDOW", master.destroy)
    app = Application(master)
    app.mainloop()

if __name__ == '__main__':
    main()