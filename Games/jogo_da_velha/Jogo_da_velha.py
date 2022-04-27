from tkinter import *

class jogo_da_velha:()

    def __init__(self):
        self.janela = Tk()
        self.janela.title("Jogo da Velha")
        self.janela.geometry("1200x1600+2500+210")
        #self.janela.resizable(0, 0)
        self.janela.config(bg="pink")       
      # Frame com o titulo do jogo da Velha
        self.frame1 = Frame(self.janela, bg="yellow")
        self.frame1.pack(side=TOP)
        self.titulo = Label(self.frame1, text="Jogo da Velha", font="Arial 37 bold", bg="black", fg="white", width=800)
        self.titulo.pack(pady=2, side=TOP)
        self.PLacar = Frame(self.janela, bg="pink", width=800, height=50)
        self.PLacar.pack(pady=16, side=TOP)
    
        self.Pontos_jogador1 = Label(self.PLacar, text="00", font="Arial 14 bold", bg="pink", fg="black",foreground="#00BFFF")  # #00BFFF cor Azul igual o da bolinha
        self.Pontos_jogador1.pack(side="left", padx=145)
        self.Pontuaçao = Label(self.PLacar, text="          Pontuaçao          ", font="Arial 15 bold", bg="pink", fg="black")
        self.Pontuaçao.pack(side=LEFT, padx=1)
        self.Pontos_jogador2 = Label(self.PLacar, text="00", font="Arial 14 bold", bg="pink", fg="black",foreground="#B33333")  # #B33333 cor vermelho igual o do X
        self.Pontos_jogador2.pack(side=RIGHT, padx=145)
      # Frame dos 9 Quadrados das jogadas
        self.frame_Quadrados_das_jogadas = Frame(self.janela, bg="black", width=50, height=50)
        self.frame_Quadrados_das_jogadas.pack(pady=5, side=TOP)
        self.botao_1 = Button(self.frame_Quadrados_das_jogadas, highlightbackground="pink", bg="pink", width=20, height=12)
        self.botao_1.grid(pady=2, padx=2, column=0, row=0)
        self.botao_2 = Button(self.frame_Quadrados_das_jogadas, highlightbackground="pink", bg="pink",  width=20, height=12)
        self.botao_2.grid(pady=2, padx=2,  column=0, row=1)
        self.botao_3 = Button(self.frame_Quadrados_das_jogadas, highlightbackground="pink", bg="pink",  width=20, height=12)
        self.botao_3.grid(pady=2, padx=2,  column=0, row=2)
        self.botao_4 = Button(self.frame_Quadrados_das_jogadas, highlightbackground="pink", bg="pink",  width=20, height=12)
        self.botao_4.grid(pady=2, padx=2,  column=1, row=0)
        self.botao_5 = Button(self.frame_Quadrados_das_jogadas, highlightbackground="pink", bg="pink",  width=20, height=12)
        self.botao_5.grid(pady=2, padx=2,  column=1, row=1)
        self.botao_6 = Button(self.frame_Quadrados_das_jogadas, highlightbackground="pink", bg="pink",  width=20, height=12)
        self.botao_6.grid(pady=2, padx=2,  column=1, row=2)
        self.botao_7 = Button(self.frame_Quadrados_das_jogadas, highlightbackground="pink", bg="pink",  width=20, height=12)
        self.botao_7.grid(pady=2, padx=2,  column=2, row=0)
        self.botao_8 = Button(self.frame_Quadrados_das_jogadas, highlightbackground="pink", bg="pink",  width=20, height=12)
        self.botao_8.grid(pady=2, padx=2,  column=2, row=1)
        self.botao_9 = Button(self.frame_Quadrados_das_jogadas, highlightbackground="pink", bg="pink",  width=20, height=12)
        self.botao_9.grid(pady=2, padx=2,  column=2, row=2)       
      # Frame da Minha Assinatura
        self.minhaAssinatura = Frame(self.janela, bg="yellow", height=9)
        self.minhaAssinatura.pack(side=BOTTOM)             
        self.Assinatura_Rodape = Label(self.minhaAssinatura, text="Criado por: Mauri Sebastiao da Luz", font="Arial 11", bg="black", fg="white", width=800)
        self.Assinatura_Rodape.pack(pady=6, side=BOTTOM)
      # Frame do Botão Add Nomes dos Jogadores
        self.Frame_do_Botão_Add_Nomes_dos_Jogadores = Frame(self.janela, bg="pink", width=800)
        self.Frame_do_Botão_Add_Nomes_dos_Jogadores.pack(pady=37)
      # Logo 0 32x32        
        logoBola = PhotoImage(file="/home/mauri/Documentos/GitHub/Software free/Games/jogo_da_velha_zilda/CIRCULO32x32.png")
        self.LabelBola_Label = Label(self.Frame_do_Botão_Add_Nomes_dos_Jogadores, image=logoBola, bg="pink")
        self.LabelBola_Label.pack(padx=1, side=LEFT)
      # Jogador 1 do rodape        
        self.Jogador_1 = Label(self.Frame_do_Botão_Add_Nomes_dos_Jogadores, text="Jogador 1 ", font="Arial 14 bold", bg="pink", fg="black")
        self.Jogador_1.pack(padx=10, side=LEFT)
      # Botao Add Nomes dos Jogadores        
        self.Adicione_os_Jogadores = Button(self.Frame_do_Botão_Add_Nomes_dos_Jogadores, text="Nomes dos Jogadores", font="Arial 12 bold", fg="white", highlightbackground="pink",  bg="black", width=19,command=lambda:self.tela_Cadastro_de_jogadores())
        self.Adicione_os_Jogadores.pack(padx=67, side=LEFT)
      # Jogador 2 do rodape        
        self.Jogador_2 = Label(self.Frame_do_Botão_Add_Nomes_dos_Jogadores, text="Jogador 2 ", font="Arial 14 bold", bg="pink", fg="black")
        self.Jogador_2.pack(padx=1, side=LEFT)
      # Logo X 32x32        
        logoX = PhotoImage(file="/home/mauri/PYTHON/venv/Games/jogo_da_velha_zilda/xXx32x32.png")
        self.simbolo_X = Label(self.Frame_do_Botão_Add_Nomes_dos_Jogadores,image=logoX, font="Arial 14 bold", bg="pink", fg="black")
        self.simbolo_X.pack(padx=10, side=LEFT)
        self.janela.mainloop()

#       ***************Tela de cadastro dos jogadores****************
   
    def tela_Cadastro_de_jogadores(self):

      # Criação da janela tela  cadastro de jogadores             
        self.cadastro = Toplevel()
        self.cadastro.title("Cadastrar Nome dos jogadores")
        self.cadastro.geometry("650x420+2775+840")
        self.cadastro.resizable(0, 0)
        self.cadastro.config(bg="pink")
      # Criação da Franes tela  cadastro de jogadores
        self.Frame_Botao_iniciar_Jogo = Frame(self.cadastro, bg="red")
        self.Frame_Botao_iniciar_Jogo.pack(side=BOTTOM, pady=25)
        self.Frame_cadastro_dos_jogadores = Frame(self.cadastro, bg="pink", height=9)
        self.Frame_cadastro_dos_jogadores.pack(side=BOTTOM, pady=1)
        self.Frame_entrada_de_nomes = Frame(self.cadastro, bg="pink", height=9, width=600)
        self.Frame_entrada_de_nomes.pack(pady=2, side=BOTTOM)
      # Entry --> entrada de nome do jogador      
        self.entrada_nome_do_jogador1 = Entry(self.Frame_entrada_de_nomes, font="Arial 14 bold", width=11)
        self.entrada_nome_do_jogador1.pack(side=LEFT, padx=40, pady=1)
        self.entrada_nome_do_jogador2 = Entry(self.Frame_entrada_de_nomes, font="Arial 14 bold", width=11)
        self.entrada_nome_do_jogador2.pack(side=RIGHT, padx=40, pady=1)       
      # Label de cadastro dos jogadores
        self.jogador1 = Label(self.Frame_cadastro_dos_jogadores, text="Jogador  1", font="Arial 12 bold", bg="pink", fg="black")
        self.jogador1.pack(side=LEFT,pady=14, padx        self.Assinatura_Rodape = Label(self.minhaAssinatura, text="Criado por: Mauri Sebastiao da Luz", font="Arial 11",  bg="black", fg="white", width=800)
=67)
        self.jogador2 = Label(self.Frame_cadastro_dos_jogadores, text="Jogador  2", font="Arial 12 bold", bg="pink", fg="black")
        self.jogador2.pack(side=RIGHT,pady=14, padx=67)
      # Icones grandes 90x90 Cadastro dos jogadores
        self.icones = Frame(self.cadastro, bg="pink", height=7, width=600)
        self.icones.pack(side=TOP, pady=30)
        self.icone_0 = PhotoImage(file="/home/mauri/PYTHON/icons/CIRCULO90x90.png")
        self.icone_0_Label = Label(self.icones, image=self.icone_0, bg="pink")
        self.icone_0_Label.pack(padx=115, pady=20, side=LEFT)
        self.icone_X = PhotoImage(file="/home/mauri/PYTHON/icons/xXx90x90.png")
        self.icone_X_label = Label(self.icones, image=self.icone_X, bg="pink")
        self.icone_X_label.pack(padx=115, pady=20, side=RIGHT)
      # Botão Cadastrar cadastro de jogadores
        self.btnCadastrar = Button(self.Frame_Botao_iniciar_Jogo, text="Cadastrar e Jogar", font="Arial 12 bold", fg="white", highlightbackground="pink",  bg="black", width=30)
        self.btnCadastrar.pack(side=BOTTOM)

jogo_da_velha()
