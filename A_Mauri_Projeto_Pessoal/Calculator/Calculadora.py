from ctypes.wintypes import SIZE
import os
os.system('clear') or None


from tkinter import *


class Calc:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculadora")
        self.window.resizable(0,0)
        self.window.background = "#376d7d"


# Icone Calculadora
        self.icon = PhotoImage('File= /mauri/PYTHON/venv/Dev_APP_tkinter/Calc/icon/calculator_22694.ico')


# Display que aparece o resultado
        self.screen_numbers = Entry(self.window, font="Arial 26 bold", bg="#376d7d", fg="black", width=31)
        self.screen_numbers.pack(pady=5)


# Frames
        self.frame1 = Frame(self.window, bg="#376d7d")
        self.frame1.pack()
        self.frame2 = Frame(self.window, width=27, height=4)
        self.frame2.pack(pady=5)
        

# Assinatura no Rodapé
        self.Assinatura = Label(self.frame2, text="M a u r i      S e b a s t i a o     d a     L u z", font="ubuntu 11", bg="#376d7d", fg="black",  width=74, height=2)
        self.Assinatura.pack()


# numeros de 0 a 9
        
        self.button_0 = Button(self.frame1, bg="orange", bd=2, text="0", 
        font="Arial 20 bold", fg="white", width=22, height=3, command=lambda: self.touch("0"))
        
        self.button_1 = Button(self.frame1, bg="orange", bd=2, text="1", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("1"))
        
        self.button_2 = Button(self.frame1, bg="orange", bd=2, text="2", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("2"))
        
        self.button_3 = Button(self.frame1, bg="orange", bd=2, text="3", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("3"))
        
        self.button_4 = Button(self.frame1, bg="orange", bd=2, text="4", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("4"))
        
        self.button_5 = Button(self.frame1, bg="orange", bd=2, text="5", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("5"))
        
        self.button_6 = Button(self.frame1, bg="orange", bd=2, text="6", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("6"))
        
        self.button_7 = Button(self.frame1, bg="orange", bd=2, text="7", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("7"))
        
        self.button_8 = Button(self.frame1, bg="orange", bd=2, text="8", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("8"))
        
        self.button_9 = Button(self.frame1, bg="orange", bd=2, text="9", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("9"))
        
        self.button_soma = Button(self.frame1, bg="orange", bd=2, text="+", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("+"))
        
        self.button_subtracao = Button(self.frame1, bg="orange", bd=2, text="-", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("-"))
        
        self.button_multiplicaçao = Button(self.frame1, bg="orange", bd=2, text="x", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("*"))
        
        self.button_divisao = Button(self.frame1, bg="orange", bd=2, text="/", 
        font="Arial 20 bold", fg="white", width=6, height=3, command=lambda: self.touch("/"))
        
        self.button_clean = Button(self.frame1, bg="orange", bd=2, text="C", 
        font="Arial 20 bold", fg="white", width=14, height=3, command=self.Clean)
        
        self.button_igual = Button(self.frame1, bg="orange", bd=2, text="=", 
        font="Arial 20 bold", fg="white", width=14, height=3, command=self.total)


# Botoes + - x /
        self.button_soma.grid(row=1, column=3)
        self.button_subtracao.grid(row=1, column=4)
        self.button_multiplicaçao.grid(row=2, column=3)
        self.button_divisao.grid(row=2, column=4)


# Botoes Limpar e igual        
        self.button_clean.grid(row=0, columnspan=2, column=3)
        self.button_igual.grid(row=3, columnspan=2, column=3)


# numeros de 0 a 9

      # Esse columnspan=2 quer dizer que o sinal de
      # igual vai ocupar 2 colunas na grade

        self.button_0.grid(row=3, columnspan=3)
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)


# Loop para manter a janela Aberta'''
        self.window.mainloop()


# Funcoes
    def touch(self, num):
        self.screen_numbers.insert(END, num)
    def Clean(self):
        self.screen_numbers.delete(0, END)
    def total(self):
        
# eval é um metodo matematico
         t = eval(self.screen_numbers.get())
         self.screen_numbers.delete(0, END)
         self.screen_numbers.insert(0, str(t))


Calc()