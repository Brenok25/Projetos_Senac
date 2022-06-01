# farenheight = C * 1.8 + 32

from tkinter import *

root = Tk()

root.geometry('330x100') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 
root.config(background='#fff') #baclground color


# Responsivo
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)



def convert():

    if entrada.get().replace(".","",1).isdigit():      
        x = (float(entrada.get()) * 1.8) +32
        saida['text'] = x      
    else:
        saida['text'] = "Tente novamente"



title = Label(root, text="Conversor")
lb1 = Label(root, text="C")
entrada= Entry(root, font="Georgia")
exect = Button(root, text="Executar", command=convert)
lb2= Label(root, text="F")
saida = Label(root, text=" Resultado ")

title.grid()
lb1.grid()
lb2.grid()
exect.grid(row=1, column=2)
entrada.grid(row=1,column=1)
saida.grid(row=2, column=1)


root.mainloop()