from tkinter import *

# Criar janela 
root = Tk()
root.geometry('500x300') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 
root.config(background='#fff') #baclground color
root.minsize(width=200, height=300)
root.maxsize(width=600, height=600)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=1)


def calc():
    if kg.get().replace(".","",1).isdigit() and alt.get().replace(".", "", 1).isdigit():
        x = round(float(kg.get()) / (float(alt.get())**2),2)
        lb4['text'] = x   

        if x <18.5:
            lb5['text'] = "Abaixo do peso"
        elif x >18.5 and x < 24.9:
            lb5['text'] = "Peso ideal"
        elif x > 25 and x < 29.9:
            lb5['text'] = "Sobrepeso"
        elif x > 30 and x < 34.9:
            lb5['text'] = "Obesidade grau I"
        elif x > 35 and x < 39.9:
            lb5['text'] = "Obesidade grau II"
        else:
            lb5['text'] = "Obesidade grau III"
 

    else:
        lb4['text'] = "Tente novamente"



lb1 = Label(root, text="Calcule seu IMC", font="Georgia 15")

lb2 = Label(root, text="Digite seu peso")

kg = Entry(root, font='Georgia', width=15)

lb3 = Label(root, text="Digite sua altura")

alt = Entry(root, font='Georgia', width=15)

bt1 = Button(root, text="Calcular", command=calc, width=15)

lb4 = Label(root, text="Seu imc", font="Georgia 10", pady=10)

lb5 = Label(root, text="Teste agora", font="Georgia 10", pady=10)



# Organizar os Widgets 
lb1.grid(row=0, column=0, sticky=NSEW)
lb2.grid(row=1, column=0, sticky=NSEW)
kg.grid(row=1, column=0)
lb3.grid(row=3, column=0, sticky=NSEW)
alt.grid(row=4, column=0)
bt1.grid(row=5, column=0)
lb4.grid(row=6, column=0, sticky=NSEW)
lb5.grid(row=7, column=0, sticky=NSEW)


# Executar e manter tabela
root.mainloop()