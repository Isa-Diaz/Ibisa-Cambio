##----Olá sejam Bem - vindo(a) ao meu codigo, espero que gostem ---- Ass: ISA
import requests
from tkinter import *
import os
from tkinter import messagebox

#-------buscando dados atuais--------
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()

cotacao_dolar = requisicao_dic['USDBRL']['bid']
cotacao_euro = requisicao_dic['EURBRL']['bid']
cotacao_btc = requisicao_dic['BTCBRL']['bid']

dolar_atual = float(cotacao_dolar)
euro_atual = float(cotacao_euro)
#--------funções------------------
def converter():
    try:
        if caixa_de_texto_real.get() == '' and caixa_de_texto_euro.get() == '':
            dolar = float(caixa_de_texto_dolar.get())
            
            real = dolar * dolar_atual
            caixa_de_texto_real.insert(0,round(real,4))
          
            euro = real / euro_atual
            caixa_de_texto_euro.insert(0,round(euro,4))
            
        elif caixa_de_texto_dolar.get() == '' and caixa_de_texto_euro.get() == '':
            real = float(caixa_de_texto_real.get())
            
            dolar = real / dolar_atual
            caixa_de_texto_dolar.insert(0, round(dolar,4))
            
            euro = real / euro_atual
            caixa_de_texto_euro.insert(0,round(euro,4))
        
        elif caixa_de_texto_real.get() == '' and caixa_de_texto_dolar.get() == '':
            
            euro = float(caixa_de_texto_euro.get())
            
            real = euro * euro_atual
            caixa_de_texto_real.insert(0,round(real,3))
            
            dolar = real / dolar_atual
            caixa_de_texto_dolar.insert(0, round(dolar,3))
            
            
            
        
    except ValueError:      
        messagebox.showerror('Atenção', 'Erro: favor inserir um valor real (verifique se usou letras ou virgulas)')

pastaJanela = os.path.dirname(__file__)

def limpar():
    caixa_de_texto_dolar.delete(0,END)
    caixa_de_texto_real.delete(0,END)
    caixa_de_texto_euro.delete(0,END)
    
#-----criando a janela -----------------
janela = Tk()
janela.title('Ibisa Câmbio')
janela.geometry('400x800')
janela.config(bg= '#FFFFFF')

imgLogo = PhotoImage(file=pastaJanela+"\\log.png")
imgLogo = imgLogo.subsample(2,2)
l_logo=Label(janela,image=imgLogo, bg= '#FFFFFF')
l_logo.place(x=80,y=2)

#-----criando local de pesquisa---------
frame_dolar = Frame(janela, borderwidth= 1.0, relief='solid', bg= '#FFFFFF')
label_dolar = Label(janela, text='Dolar', bg= '#FFFFFF')
caixa_de_texto_dolar = Entry(frame_dolar, width=30)
frame_dolar.place(x=105, y=280, width=195, height= 45)
label_dolar.place(x=120, y=280)
caixa_de_texto_dolar.place(x=5, y=15)

frame_real = Frame(janela, borderwidth= 1.0, relief='solid', bg= '#FFFFFF')
label_real = Label(janela, text='Real', bg= '#FFFFFF')
caixa_de_texto_real = Entry(frame_real, width=30)
frame_real.place(x=105, y=340, width=195, height= 45)
label_real.place(x=120, y=340)
caixa_de_texto_real.place(x=5, y=15)

frame_euro = Frame(janela, borderwidth= 1.0, relief='solid', bg= '#FFFFFF')
label_euro = Label(janela, text='Euro', bg= '#FFFFFF')
caixa_de_texto_euro = Entry(frame_euro, width=30)
frame_euro.place(x=105, y=400, width=195, height= 45)
label_euro.place(x=120, y=400)
caixa_de_texto_euro.place(x=5, y=15)

#-----------imagens nos Botões-----------------------
limpesa = PhotoImage(file=pastaJanela+"\\limpesa(2).png")
limpesa = limpesa.subsample(6,6)
limpesa1 = Label(image = limpesa)

converte = PhotoImage(file=pastaJanela+"\\convert.png")
converte = converte.subsample(3,3)
converte1 = Label(image = converte)

botao_converter = Button(janela, image= converte, font=('Georgia', 15), highlightthickness=0, bd = 0, command=converter)

botao_limpar= Button(janela, image = limpesa, font=('Georgia', 15), highlightthickness=0, bd = 0, command=limpar)

botao_converter.place(x=115, y=445)
botao_limpar.place(x=292, y=455)

#------Imagem final-------------
imgbase = PhotoImage(file=pastaJanela+"\\fund.png")
imgbase = imgbase.subsample(1,1)
l_base=Label(janela,image=imgbase, bg= '#FFFFFF')
l_base.place(x=0,y=670)
janela.mainloop()