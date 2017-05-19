# -*- coding: utf-8 -*-

from geren_babas import *
from Tkinter import *

class ApplicationCrianca:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        
        self.titulo = Label(self.container1, text="Opções para criança:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()
        
        self.lblidcrianca = Label(self.container2, text="ID da criança:", font=self.fonte, width=13)
        self.lblidcrianca.pack(side=LEFT)
        
        self.txtidcriancatextvariable = StringVar(self.container2)
        self.txtidcriancatextvariable.trace("w", lambda name, index, mode: self.charLimiter(self.txtidcriancatextvariable))
        
        self.txtidcrianca = Entry(self.container2, width=30, textvariable=self.txtidcriancatextvariable)  
        self.txtidcrianca["width"] = 11
        self.txtidcrianca["font"] = self.fonte
        self.txtidcrianca.pack(side=LEFT)
        
        
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarCrianca
        self.btnBuscar.pack(side=RIGHT)
        
        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        
        self.txtnometextvariable = StringVar(self.container3)
        self.txtnometextvariable.trace("w", lambda name, index, mode: self.charLimiter2(self.txtnometextvariable))
   
        self.txtnome = Entry(self.container3, width=30, textvariable=self.txtnometextvariable)
        self.txtnome["width"] = 40
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)
   
        self.lblidade = Label(self.container4, text="Idade:", font=self.fonte, width=10)
        self.lblidade.pack(side=LEFT)
   
        self.txtidadetextvariable = StringVar(self.container4)
        self.txtidadetextvariable.trace("w", lambda name, index, mode: self.charLimiter(self.txtidadetextvariable))
        
        self.txtidade = Entry(self.container4, width=30, textvariable=self.txtidadetextvariable)
        self.txtidade["width"] = 40
        self.txtidade["font"] = self.fonte
        self.txtidade.pack(side=LEFT)
   
        self.lblcpfcrianca= Label(self.container5, text="CPF:", font=self.fonte, width=10)
        self.lblcpfcrianca.pack(side=LEFT)
        
        self.txtcpfcriancatextvariable = StringVar(self.container5)
        self.txtcpfcriancatextvariable.trace("w", lambda name, index, mode: self.charLimiter3(self.txtcpfcriancatextvariable))
   
        self.txtcpfcrianca = Entry(self.container5, width=30, textvariable=self.txtcpfcriancatextvariable)
        self.txtcpfcrianca["width"] = 40
        self.txtcpfcrianca["font"] = self.fonte
        self.txtcpfcrianca.pack(side=LEFT)
   
        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirCrianca
        self.bntInsert.pack (side=LEFT)
   
        self.bntAlterar = Button(self.container8, text="Atualizar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarCrianca
        self.bntAlterar.pack (side=LEFT)
   
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirCrianca
        self.bntExcluir.pack(side=LEFT)
   
        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
        

    def charLimiter(self, text):
        text.set(text.get()[0:3])
        
    def charLimiter2(self, text):
        text.set(text.get()[0:40])
        
    def charLimiter3(self, text):
        text.set(text.get()[0:11])    

    def inserirCrianca(self):
        
        crianca = Crianca(self.txtidcrianca.get(), self.txtnome.get(), self.txtidade.get(), self.txtcpfcrianca.get())
        
        sucesso = criarCrianca(crianca)
        
        if (sucesso == True):
            self.lblmsg["text"] = "Criança cadastrada!"
        else:
            self.lblmsg["text"] = "Erro! Não foi possível cadastradar a crianca!"
        
        self.txtidcrianca.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtidade.delete(0, END)
        self.txtcpfcrianca.delete(0, END)
        
    def alterarCrianca(self):
        crianca = consultarCrianca(self.txtidcrianca.get())
        if (crianca != None):
            nome = self.txtnome.get()
            if (nome != None and nome != ""):
                crianca.nome = nome
            
            idade = self.txtidade.get()
            if (idade != None and idade != ""):
                crianca.idade = idade
            
            cpfcrianca = self.txtcpfcrianca.get()
            if (cpfcrianca != None and cpfcrianca != ""):
                crianca.cpf = cpfcrianca
            alt = atualizarCrianca(crianca.id, crianca)
            if (alt == True):
                self.lblmsg["text"] = "Dado(s) atualizados!"
            else:
                self.lblmsg["text"] = "Erro! Não foi possível atualizar"
        else: 
            self.lblmsg["text"] = "Erro! Criança não encontrada para atualização"
       
        self.txtidcrianca.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtidade.delete(0, END)
        self.txtcpfcrianca.delete(0, END)
     
    def excluirCrianca(self):
       
        idcrianca = self.txtidcrianca.get()
        resultado = deletarCrianca(idcrianca)
        if (resultado == True):
            self.lblmsg["text"] = "Criança Deletada!"
        else:
            self.lblmsg["text"] = "Erro! Não houve exclusão! Criança pode não está cadastrada"
       
        self.txtidcrianca.delete(0, END)       
       
    def buscarCrianca(self):
       
        idcrianca = self.txtidcrianca.get()
        resultado = consultarCrianca(idcrianca)
        if (resultado != None):
            self.lblmsg["text"] = resultado
        else:
            self.lblmsg["text"] = "Criança não encontrada!"
       
        self.txtidcrianca.delete(0, END)
              
     
#root = Tk()
#root.wm_title("Gerenciamento de Babas")
#ApplicationCrianca(root)
#root.mainloop()
    
