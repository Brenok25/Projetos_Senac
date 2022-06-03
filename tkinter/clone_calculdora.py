from tkinter import *
from turtle import color

root= Tk()
root.geometry('320x500') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 
root.config(background='#fff') #baclground color
root.minsize(width=320, height=500)
root.maxsize(width=800, height=500)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)


# #functions
def entrada(valor):#função pra ir colocando na frente indinitamente 
    result['text'] += valor

def limpar(): #função para limpar
    result['text'] = ""

def resultado():
    x=eval(result['text'])
    result['text']=x



#widgets
root.title('Calculadora')
result = Label(root, text="", background="Black", fg="green", font="40")

#numeros
num9 = Button(root, text="9", height=1, command=lambda: entrada('9'), font="Sans-Serif 20")
num8 = Button(root, text="8", height=1, command=lambda: entrada('8'), font="Sans-Serif 20")
num7 = Button(root, text="7", height=1, command=lambda: entrada('7'), font="Sans-Serif 20")
num6 = Button(root, text="6", height=1, command=lambda: entrada('6'), font="Sans-Serif 20")
num5 = Button(root, text="5", height=1, command=lambda: entrada('5'), font="Sans-Serif 20")
num4 = Button(root, text="4", height=1, command=lambda: entrada('4'), font="Sans-Serif 20")
num3 = Button(root, text="3", height=1, command=lambda: entrada('3'), font="Sans-Serif 20")
num2 = Button(root, text="2", height=1, command=lambda: entrada('2'), font="Sans-Serif 20")
num1 = Button(root, text="1", height=1, command=lambda: entrada('1'), font="Sans-Serif 20")
num0 = Button(root, text="0", height=1, command=lambda: entrada('0'), font="Sans-Serif 20")

#funcionalidades
ccc = Button(root, text="C", height=1,command= limpar, font="Sans-Serif 20")
soma = Button(root, text="+", height=1, command=lambda: entrada('+'), font="Sans-Serif 20")
subtr = Button(root, text="-", height=1, command=lambda: entrada('-'), font="Sans-Serif 20")
div = Button(root, text="/", height=1, command=lambda: entrada('/'), font="Sans-Serif 20")
pont = Button(root, text=".", height=1, command=lambda: entrada('.'), font="Sans-Serif 20")
igual = Button(root, text="=", height=1, font="Sans-Serif 20", command=resultado)

#Apresentar Layout
#Linha 0
result.grid(row=0, column=0,columnspan=4, sticky=NSEW)

#Linha 1 
num7.grid(row=1, column=0, sticky=NSEW)
num8.grid(row=1,  column=1, sticky=NSEW)
num9.grid(row=1,  column=2, sticky=NSEW)
div.grid(row=1,  column=3, sticky=NSEW)

#Linha 2 
num4.grid(row=2,  column=0, sticky=NSEW)
num5.grid(row=2, column=1, sticky=NSEW)
num6.grid(row=2,  column=2, sticky=NSEW)
subtr.grid(row=2,  column=3, sticky=NSEW)

#Linha 3
num1.grid(row=3,  column=0, sticky=NSEW)
num2.grid(row=3,  column=1, sticky=NSEW)
num3.grid(row=3,  column=2, sticky=NSEW)
soma.grid(row=3,  column=3, sticky=NSEW)


#Linha 4
num0.grid(row=4,  column=0, sticky=NSEW)
pont.grid(row=4,  column=1, sticky=NSEW)
ccc.grid(row=4,  column=2, sticky=NSEW)
igual.grid(row=4,  column=3, sticky=NSEW)


root.bind("1", lambda event: entrada('1') )
root.bind("2", lambda event: entrada('2') )
root.bind("3", lambda event: entrada('3') )
root.bind("4", lambda event: entrada('4') )
root.bind("5", lambda event: entrada('5') )
root.bind("6", lambda event: entrada('6') )
root.bind("7", lambda event: entrada('7') )
root.bind("8", lambda event: entrada('8') )
root.bind("9", lambda event: entrada('9') )
root.bind("0", lambda event: entrada('0') )
root.bind("+", lambda event: entrada('+') )
root.bind("-", lambda event: entrada('-') )
root.bind(".", lambda event: entrada('.') )
root.bind("/", lambda event: entrada('/') )
root.bind("=", lambda event: resultado() )
root.bind("<Return>", lambda event: resultado() )
root.bind("<Escape>", lambda event: limpar() )

#Manter 
root.mainloop()