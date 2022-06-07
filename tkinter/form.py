from tkinter import *
from turtle import back
from mysqlx import Row

from pyparsing import col


root = Tk()
root.geometry('730x220+720+350') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir 
root.config(background='#fff') #background color
root.minsize(width=730, height=230)
root.maxsize(width=730, height=250)
#responsividade // ver uma maneira mais facil de colocar
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
root.grid_columnconfigure(6, weight=1)
root.grid_columnconfigure(7, weight=1)
root.grid_columnconfigure(8, weight=1)
root.grid_columnconfigure(9, weight=1)
root.grid_columnconfigure(10, weight=1)
root.grid_columnconfigure(11, weight=1)
root.grid_columnconfigure(12, weight=1)
root.grid_columnconfigure(13, weight=1)

root.title('Formulario')


#frames
fr1 = LabelFrame(root, background='#fff', text='Todos os dados a seguir são obrigatorios')
fr2 = Frame(root, background='#fff')
fr3 = Frame(root, background='#fff')

#widgts frame 1 
title_fr1 = Label(fr1, text="  Dados pessoais", fg="blue", font='Georgia 12')

name_fr1 = Label(fr1, text="Nome:", font='Georgia 10')
name_e_fr1 = Entry(fr1, fg='blue', font='Georgia 10')

date_fr1 = Label(fr1, text="Data Nasc:", font='Georgia 10')
date_e_fr1 = Entry(fr1, fg='blue', font='Georgia 10')

cpf_fr1 = Label(fr1, text="CPF:", font='Georgia 10')
cpf_e_fr1 = Entry(fr1, fg='blue', font='Georgia 10')

tel_fr1 = Label(fr1, text="Telefone:", font='Georgia 10')
tel_e_fr1 = Entry(fr1, fg='blue', font='Georgia 10', width=10)

#widgts frame 2
title_fr2 = Label(fr1, text="Endereço", fg="blue", font='Georgia 12')

rua_fr2 = Label(fr1, text="Rua:", font='Georgia 10')
rua_e_fr2 = Entry(fr1, fg='blue', font='Georgia 10')

num_fr2 = Label(fr1, text="N°:", font='Georgia 10') # ° == Alt Gr + ?
num_e_fr2 = Entry(fr1, fg='blue', font='Georgia 10', width=10)

bairro_fr2 = Label(fr1, text="Bairro:", font='Georgia 10')
bairro_e_fr2 = Entry(fr1, fg='blue', font='Georgia 10')

city_fr2 = Label(fr1, text="Cidade:", font='Georgia 10')
city_e_fr2 = Entry(fr1, fg='blue', font='Georgia 10')

uf_fr2 = Label(fr1, text="UF:", font='Georgia 10')
uf_e_fr2 = Entry(fr1, fg='blue', font='Georgia 10', width=10)

#widgts frame 2
save_fr3 = Button(fr3, text="Gravar Dados", font='Georfia 10')
lista_fr3 = Button(fr3, text="Listar Dados", font='Georfia 10')


#mostar
fr1.grid()
fr2.grid()
fr3.grid(pady=15,padx= 15, sticky=W)

#mostrar widgts frame 1
#linha 0
title_fr1.grid(row=0, column=0) 

#linha 1
name_fr1.grid(row=1, column=0, sticky=W, padx = 10 )
name_e_fr1.grid(row=1, column=1, columnspan=16, sticky=NSEW)

#linha 2

cpf_fr1.grid(row=2, column=0, sticky=W, padx = 10)
cpf_e_fr1.grid(row=2, column=1, columnspan=4, sticky=NSEW)

date_fr1.grid(row=2, column=5)
date_e_fr1.grid(row=2, column=7, columnspan=4, sticky=NSEW)

tel_fr1.grid(row=2, column=12)
tel_e_fr1.grid(row=2, column=13, columnspan=4, sticky=NSEW)


#mostrar widgts frame 2
#linha 5
title_fr2.grid(row=5, column=0, sticky=W, padx = 10) 

#linha 6
rua_fr2.grid(row=6, column=0, sticky=W, padx = 10)
rua_e_fr2.grid(row=6, column=1, columnspan=10, sticky=NSEW)

num_fr2.grid(row=6, column=12)
num_e_fr2.grid(row=6, column=13, sticky=NSEW)

#linha 7
bairro_fr2.grid(row=7, column=0, sticky=W, padx = 10)
bairro_e_fr2.grid(row=7, column=1, columnspan=4, sticky=NSEW)

city_fr2.grid(row=7, column=5)
city_e_fr2.grid(row=7, column=7, columnspan=4, sticky=NSEW)

uf_fr2.grid(row=7, column=12)
uf_e_fr2.grid(row=7, column=13, columnspan=2, sticky=NSEW)


#mostrar widgts frame 2
save_fr3.grid(row=8, column=0)
lista_fr3.grid(row=8, column=1)

root.mainloop()