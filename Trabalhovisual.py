from tkinter import * #biblioteca grafica

######## funções ########

def exibirtxt():
    
    nome = str(caixa.get()) #armazenar o nome
    txt = str (caixa2.get()) # armazenar o texto
    texto3['text'] = nome + ' Disse ' + txt
    
    
######## comandos basicos para abrir uma janela ########

janela = Tk()
janela.title('coletor')
janela.geometry("155x150")

########  texto que vai em cada coisa  ########

texto1 = Label(janela, text = "digite o seu nome:") #basicamente texto
caixa = Entry(janela) #coletar informação
texto2 = Label(janela, text = "digite oque voce quer dizer:") #basicamente texto
caixa2 = Entry(janela) #coletar informação
botao = Button(janela, text = "exibir", command = exibirtxt ) #exibir função texto3
texto3 = Label(janela, text = "" ) #aonde vai exibir

######## parte visual e onde vai ficar cada coisa ########

texto1.grid()
caixa.grid()
texto2.grid()
caixa2.grid()
botao.grid()
texto3.grid()

######## Atualizar a janela quando algo mudar ########

janela.mainloop()
