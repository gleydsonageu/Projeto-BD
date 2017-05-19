# -*- coding: utf-8 -*-

from geren_babas import *
from Tkinter import *

class Application:
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
        
        self.titulo = Label(self.container1, text="Opções para cliente:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()
        
        self.lblcpfcliente = Label(self.container2, text="CPF do cliente:", font=self.fonte, width=13)
        self.lblcpfcliente.pack(side=LEFT)
        
        self.txtcpfclientetextvariable = StringVar(self.container2)
        self.txtcpfclientetextvariable.trace("w", lambda name, index, mode: self.charLimiter(self.txtcpfclientetextvariable))
        
        self.txtcpfcliente = Entry(self.container2, width=11, textvariable=self.txtcpfclientetextvariable)  
        self.txtcpfcliente["font"] = self.fonte
        self.txtcpfcliente.pack(side=LEFT)
        
        
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarCliente
        self.btnBuscar.pack(side=RIGHT)
        
        self.lblnome_cli = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome_cli.pack(side=LEFT)
        
        self.txtnome_clitextvariable = StringVar(self.container3)
        self.txtnome_clitextvariable.trace("w", lambda name, index, mode: self.charLimiter2(self.txtnome_clitextvariable))
   
        self.txtnome_cli = Entry(self.container3, width=30, textvariable=self.txtnome_clitextvariable)
        self.txtnome_cli["width"] = 40
        self.txtnome_cli["font"] = self.fonte
        self.txtnome_cli.pack(side=LEFT)
   
        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
   
        self.txttelefonetextvariable = StringVar(self.container4)
        self.txttelefonetextvariable.trace("w", lambda name, index, mode: self.charLimiter(self.txttelefonetextvariable))
        
        self.txttelefone = Entry(self.container4, width=30, textvariable=self.txttelefonetextvariable)
        self.txttelefone["width"] = 40
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)
   
        self.lblemail= Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        
        self.txtemailtextvariable = StringVar(self.container5)
        self.txtemailtextvariable.trace("w", lambda name, index, mode: self.charLimiter2(self.txtemailtextvariable))
   
        self.txtemail = Entry(self.container5, width=30, textvariable=self.txtemailtextvariable)
        self.txtemail["width"] = 40
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)
   
        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirCliente
        self.bntInsert.pack (side=LEFT)
   
        self.bntAlterar = Button(self.container8, text="Atualizar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarCliente
        self.bntAlterar.pack (side=LEFT)
   
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirCliente
        self.bntExcluir.pack(side=LEFT)
   
        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
        

    def charLimiter(self, text):
        text.set(text.get()[0:11])
        
    def charLimiter2(self, text):
        text.set(text.get()[0:40])    

    def inserirCliente(self):
        
        cliente = Cliente(self.txtcpfcliente.get(), self.txtnome_cli.get(), self.txttelefone.get(), self.txtemail.get())
        
        sucesso = criarCliente(cliente)
        
        if (sucesso == True):
            self.lblmsg["text"] = "Cliente cadastrado!"
        else:
            self.lblmsg["text"] = "Erro! Não foi possível cadastrar o cliente!"
        
        self.txtcpfcliente.delete(0, END)
        self.txtnome_cli.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        
    def alterarCliente(self):
        cliente = consultarCliente(self.txtcpfcliente.get())
        if (cliente != None):
            nome = self.txtnome_cli.get()
            if (nome != None and nome != ""):
                cliente.nome_cli = nome
            
            telefone = self.txttelefone.get()
            if (telefone != None and telefone != ""):
                cliente.telefone = telefone
            
            email = self.txtemail.get()
            if (email != None and email != ""):
                cliente.email = email
            alt = atualizarCliente(cliente.cpf, cliente)
            if (alt == True):
                self.lblmsg["text"] = "Dado(s) atualizados!"
            else:
                self.lblmsg["text"] = "Erro! Não foi possível atualizar"
        else: 
            self.lblmsg["text"] = "Erro! Cliente não encontrado para atualização"
       
        self.txtcpfcliente.delete(0, END)
        self.txtnome_cli.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
     
    def excluirCliente(self):
       
        cpfcliente = self.txtcpfcliente.get()
        resultado = deletarCliente(cpfcliente)
        if (resultado == True):
            self.lblmsg["text"] = "Cliente Deletado!"
        else:
            self.lblmsg["text"] = "Erro! Não houve exclusão! Cliente pode não está cadastrado"
       
        self.txtcpfcliente.delete(0, END)       
       
    def buscarCliente(self):
       
        cpfcliente = self.txtcpfcliente.get()
        resultado = consultarCliente(cpfcliente)
        if (resultado != None):
            self.lblmsg["text"] = resultado
        else:
            self.lblmsg["text"] = "Cliente não encontrado!"
       
        self.txtcpfcliente.delete(0, END)
              
     
#root = Tk()
#root.wm_title("Cliente")
#Application(root)
#root.mainloop()
    
