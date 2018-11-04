from  tkinter import *
import tkinter


janela = tkinter.Tk()
janela.title('Cálculo do IMC - indice de Massa Corporal')

lb = Label(janela, text="Nome do Paciente:")
lb.place(x=50, y=50)

lb = Label(janela, text="Endereço Completo:")
lb.place(x=50, y=80)

lb = Label(janela, text="Altura (cm)")
lb.place(x=50, y=110)

lb = Label(janela, text="Peso (KG)")
lb.place(x=50, y=135)

lb = Label(janela, text="Resultado")
lb.place(x=300, y=165)



ed = Entry()
ed.place(x=200, y=50)

ed = Entry()
ed.place(x=200, y=80)

ed =Entry()
ed.place(x=200, y=110)

ed = Entry()
ed.place(x=200, y=135)

ed=Entry()
ed.place(x=370, y=165)

bt = Button(janela, width=12, text="Caclular")
bt.place(x=200, y=200)

bt = Button(janela, width=12, text="Reniciar")
bt.place(x=300, y=200)

bt = Button(janela, width=10, text="Sair")
bt.place(x=420, y=200)





janela.geometry("800x300+100+100")


janela.mainloop()