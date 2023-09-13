from tkinter import * #biblioteca grafica

######## funções ########

def exibirtxt():
    
    nome = str(caixa.get()) #armazenar o nome
    txt = str (caixa2.get()) # armazenar o texto
    texto3['text'] = nome + ' Disse ' + txt
    
    
######## comandos basicos para abrir uma janela ########

janela = Tk()
janela.title('coletor')

########  texto que vai em cada coisa  ########

texto1 = Label(janela, text = "digite o seu nome:")
caixa = Entry(janela)
texto2 = Label(janela, text = "digite oque voce quer dizer:")
caixa2 = Entry(janela)
botao = Button(janela, text = "exibir", command = exibirtxt )
texto3 = Label(janela, text = "oi" )

######## parte visual e onde vai ficar cada coisa ########

texto1.grid()
caixa.grid()
texto2.grid()
caixa2.grid()
botao.grid()
texto3.grid()

######## Atualizar a janela quando algo mudar ########

janela.mainloop()