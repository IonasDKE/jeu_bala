from tkinter import *
from tkinter.messagebox import showinfo
# from tkinter.ttk import *
        

def mainMenu(root):
    root.title('Jeu Baladins')
    root.geometry("400x400")
    bg = PhotoImage(file='baladins.png')
    
    canvas = Canvas(root, width=400, height=400)
    canvas.pack(fill='both', expand=True)

    canvas.create_image(0,0, image=bg, anchor='nw')
    canvas.theimage = bg

    canvas.create_text(200,200, text='Etes vous pret?', font=('Helvetica', 30), fill='blue')

    openNext = Button(root, text='OUIII!!')
    openNext.bind('<Button>', lambda e: [start(root)])

    button1 = canvas.create_window(30, 30, anchor='nw', window=openNext)
    

def start(root):
    root.withdraw()
    newWind = Toplevel(root)
    newWind.protocol("WM_DELETE_WINDOW", root.destroy)
    newWind.geometry("400x800")

    bg = PhotoImage(file='cowboy.png')

    canvas1 = Canvas(newWind, width=400, height=800)
    canvas1.pack(fill='both', expand=True)

    canvas1.create_image(0,0, image=bg, anchor='nw')
    canvas1.theimage = bg
    
    canvas1.create_text(200,50, text='Question 1', font=('Helvetica', 28))
    canvas1.create_text(200,100, text='De quel couleur sont les chemises pio?', font=('Helvetica', 15), fill='black')

    ans1 = Button(newWind, text='blue claire', command=popup)
    button1 = canvas1.create_window(175, 150, anchor='nw', window=ans1)

    ans2 =Button(newWind, text='vert', command=popup)
    button2 = canvas1.create_window(175, 200, anchor='nw', window=ans2)

    ans3 = Button(newWind, text='bleu fonce', command=popup)
    button3 = canvas1.create_window(175, 250, anchor='nw', window=ans3)

    ans4 = Button(newWind, text='rouge')
    ans4.bind('<Button>', lambda e: [popupGood(), newWind.withdraw(), q2(root)])
    button4 = canvas1.create_window(175, 300, anchor='nw', window=ans4)


def q2(root):
    root.withdraw()
    newWind = Toplevel(root)
    newWind.protocol("WM_DELETE_WINDOW", root.destroy)
    newWind.geometry("400x800")

    bg = PhotoImage(file='cowboy.png')

    canvas1 = Canvas(newWind, width=400, height=800)
    canvas1.pack(fill='both', expand=True)

    canvas1.create_image(0,0, image=bg, anchor='nw')
    canvas1.theimage = bg
    
    canvas1.create_text(200,50, text='Question 2', font=('Helvetica', 28))
    canvas1.create_text(200,100, text='De quel couleur sont les chemises pio?', font=('Helvetica', 15), fill='black')

    ans1 = Button(newWind, text='blue claire', command=popup)
    button1 = canvas1.create_window(175, 150, anchor='nw', window=ans1)

    ans2 =Button(newWind, text='vert', command=popup)
    button2 = canvas1.create_window(175, 200, anchor='nw', window=ans2)

    ans3 = Button(newWind, text='bleu fonce', command=popup)
    button3 = canvas1.create_window(175, 250, anchor='nw', window=ans3)

    ans4 = Button(newWind, text='rouge')
    ans4.bind('<Button>', lambda e: [popupGood(), newWind.withdraw(), q2(root)])
    button4 = canvas1.create_window(175, 300, anchor='nw', window=ans4)


# Informe qu'une contrainte a bien ete ajoutée
def popup():
    showinfo(message="Mauvasie reponse! Reviens plus tard")

def popupGood():
    showinfo(message="BIEN JOUE!")

def main():
    master = Tk()
    master.protocol("WM_DELETE_WINDOW", master.destroy)

    mainMenu(master)

    master.mainloop()

if __name__ == '__main__':
    main()