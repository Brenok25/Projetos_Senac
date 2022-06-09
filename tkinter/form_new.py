from tkinter import *

root = Tk()
root.geometry('770x200+20+50') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#fff') #background color
root.minsize(width=770, height=200)
root.maxsize(width=800, height=250)

#Verifica se a data existe ou não
def validar():
    valida = False

    #pega o dia
    dia = (int(date_e_fr1.get()[:2]))

    #pega o mes
    mes = (int(date_e_fr1.get()[2:3]))
    if mes == 0:
        mes = (int(date_e_fr1.get()[2:4]))
        
    #pega o ano
    ano = (int(date_e_fr1.get()[4:8]))


    # Meses com 31 dias
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if (dia <= 31):
            valida = True
    # Meses com 30 dias
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if (dia <= 30):
            valida = True
    elif mes == 2:
        # Testa se é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if (dia <= 29):
                valida = True
        elif (dia <= 28):
            valida = True

    if (valida):
        print( 'Data válida')
    else:
        print( 'Data inválida')


#-------------------------- Frame 1 --------------------------

fr1 = LabelFrame(root, background='#fff', text='Dados Pessoais', fg="blue", font='Georgia 12')

name_fr1 = Label(fr1, text="Nome:", font='Georgia 10')
name_e_fr1 = Entry(fr1, fg='blue', font='Georgia 10')

date_fr1 = Label(fr1, text="Data Nasc:", font='Georgia 10')
date_e_fr1 = Entry(fr1, fg='blue', font='Georgia 10')

cpf_fr1 = Label(fr1, text="CPF:", font='Georgia 10')
cpf_e_fr1 = Entry(fr1, fg='blue', font='Georgia 10')

tel_fr1 = Label(fr1, text="Telefone:", font='Georgia 10')
tel_e_fr1 = Entry(fr1, fg='blue', font='Georgia 10')

#mostrar frame
fr1.grid(row=0, padx= 15)

#linha 1
name_fr1.grid(row=1, column=0)
name_e_fr1.grid(row=1, column=1, columnspan=5, sticky=NSEW)

#linha 2

cpf_fr1.grid(row=2, column=0)
cpf_e_fr1.grid(row=2, column=1)

date_fr1.grid(row=2, column=2)
date_e_fr1.grid(row=2, column=3)

tel_fr1.grid(row=2, column=4)
tel_e_fr1.grid(row=2, column=5)

#-------------------------- Frame 2 --------------------------

fr2 = LabelFrame(root, background='#fff', text='Endereço', fg="blue", font='Georgia 12')

rua_fr2 = Label(fr2, text="Rua:", font='Georgia 10')
rua_e_fr2 = Entry(fr2, fg='blue', font='Georgia 10')

num_fr2 = Label(fr2, text="  N° da casa:", font='Georgia 10') # ° == Alt Gr + ?
num_e_fr2 = Entry(fr2, fg='blue', font='Georgia 10')

bairro_fr2 = Label(fr2, text="Bairro:", font='Georgia 10')
bairro_e_fr2 = Entry(fr2, fg='blue', font='Georgia 10')

city_fr2 = Label(fr2, text="Cidade:", font='Georgia 10')
city_e_fr2 = Entry(fr2, fg='blue', font='Georgia 10')

uf_fr2 = Label(fr2, text=" Estado:", font='Georgia 10')
uf_e_fr2 = Entry(fr2, fg='blue', font='Georgia 10')

#mostrar widgts frame 2

fr2.grid(row=1, padx= 15, sticky=NSEW)

#linha 3
rua_fr2.grid(row=3, column=0)
rua_e_fr2.grid(row=3, column=1, columnspan=3, sticky=NSEW)

num_fr2.grid(row=3, column=4)
num_e_fr2.grid(row=3, column=5)

#linha 4
bairro_fr2.grid(row=4, column=0,)
bairro_e_fr2.grid(row=4, column=1)

city_fr2.grid(row=4, column=2)
city_e_fr2.grid(row=4, column=3)

uf_fr2.grid(row=4, column=4)
uf_e_fr2.grid(row=4, column=5)


#-------------------------- Frame 3 --------------------------

fr3 = LabelFrame(root, background='#fff', text='Finalize seu cadastro', fg="blue", font='Georgia 12')

# mostar widgts frame 3
fr3.grid(row=2, padx= 15, sticky=NSEW)

save_fr3 = Button(fr3, text="Gravar Dados", font='Georfia 10', command=validar)
lista_fr3 = Button(fr3, text="Listar Dados", font='Georfia 10')

#Linha 8
save_fr3.grid(row=8, column=0)
lista_fr3.grid(row=8, column=1)


root.mainloop()