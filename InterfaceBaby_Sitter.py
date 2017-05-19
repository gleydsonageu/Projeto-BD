# -*- coding: utf-8 -*-

from geren_babas import *
from Tkinter import *

class ApplicationBaby_Sitter:
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

        self.titulo = Label(self.container1, text="Opções para Babá:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidbabasitter = Label(self.container2, text="ID do serviço Babá:", font=self.fonte, width=16)
        self.lblidbabasitter.pack(side=LEFT)
        
        self.txtbabasittertextvariable = StringVar(self.container2)
        self.txtbabasittertextvariable.trace("w", lambda name, index, mode: self.charLimiter(self.txtbabasittertextvariable))
        
        self.txtidbabasitter = Entry(self.container2, width=3, textvariable=self.txtbabasittertextvariable)
        self.txtidbabasitter["width"] = 3  
        self.txtidbabasitter["font"] = self.fonte
        self.txtidbabasitter.pack(side=LEFT)
        
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarBaba_Sitter
        self.btnBuscar.pack(side=RIGHT)

        self.lbldatagendada = Label(self.container3, text="Data Agendada:", font=self.fonte, width=14)
        self.lbldatagendada.pack(side=LEFT)
        
        self.txtdatagendadatextvariable = StringVar(self.container3)
        self.txtdatagendadatextvariable.trace("w", lambda name, index, mode: self.charLimiter2(self.txtdatagendadatextvariable))
   
        self.txtdatagendada = Entry(self.container3, width=30, textvariable=self.txtdatagendadatextvariable)
        self.txtdatagendada["width"] = 40
        self.txtdatagendada["font"] = self.fonte
        self.txtdatagendada.pack(side=LEFT)

        self.lbldataultimotrabalho = Label(self.container4, text="Data último trabalho:", font=self.fonte, width=21)
        self.lbldataultimotrabalho.pack(side=LEFT)
        
        self.txtdataultimotrabalhotextvariable = StringVar(self.container4)
        self.txtdataultimotrabalhotextvariable.trace("w", lambda name, index, mode: self.charLimiter2(self.txtdataultimotrabalhotextvariable))
   
        self.txtdataultimotrabalho = Entry(self.container4, width=30, textvariable=self.txtdataultimotrabalhotextvariable)
        self.txtdataultimotrabalho["width"] = 40
        self.txtdataultimotrabalho["font"] = self.fonte
        self.txtdataultimotrabalho.pack(side=LEFT)

        self.lbldataatendimento = Label(self.container5, text="Data do atendimento:", font=self.fonte, width=20)
        self.lbldataatendimento.pack(side=LEFT)
        
        self.txtdataatendimentotextvariable = StringVar(self.container5)
        self.txtdataatendimentotextvariable.trace("w", lambda name, index, mode: self.charLimiter2(self.txtdataatendimentotextvariable))
   
        self.txtdataatendimento = Entry(self.container5, width=30, textvariable=self.txtdataatendimentotextvariable)
        self.txtdataatendimento["width"] = 40
        self.txtdataatendimento["font"] = self.fonte
        self.txtdataatendimento.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirBaba_Sitter
        self.bntInsert.pack (side=LEFT)
   
        self.bntAlterar = Button(self.container8, text="Atualizar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarBaba_Sitter
        self.bntAlterar.pack (side=LEFT)
   
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirBaba_Sitter
        self.bntExcluir.pack(side=LEFT)
   
        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def charLimiter(self, text):
        text.set(text.get()[0:3])
        
    def charLimiter2(self, text):
        text.set(text.get()[0:10])
# inserirBaba OK
    def inserirBaba_Sitter(self):
        baby = Baby_Sitter(self.txtidbabasitter.get(), self.txtdatagendada.get(), self.txtdataultimotrabalho.get(), self.txtdataatendimento.get())
        sucesso = criarBaby_Sitter(baby)
        
        if (sucesso == True):
            self.lblmsg["text"] = "Cadastrada!"
        else:
            self.lblmsg["text"] = "Erro! Não foi possível cadastrar babá!"
        
        self.txtidbabasitter.delete(0,END)
        self.txtdatagendada.delete(0, END)
        self.txtdataultimotrabalho.delete(0, END)
        self.txtdataatendimento.delete(0, END)
        
    def alterarBaba_Sitter(self):
        baba = consultarBaby_Sitter(self.txtidbabasitter.get(),self.txtdatagendada.get())
        if (baba != None):
            ulttrabalho = self.txtdataultimotrabalho.get()
            if (ulttrabalho != None and ulttrabalho != ""):
                baba.data_ultimo_trabalho = ulttrabalho

            dataatendimento = self.txtdataatendimento.get()
            if (dataatendimento != None and dataatendimento != ""):
                baba.data_atendimento = dataatendimento

            alt = atualizarBaby_Sitter(baba.id, baba.data_agendada, baba)
            if (alt == True):
                self.lblmsg["text"] = "Dado(s) atualizados!"
            else:
                self.lblmsg["text"] = "Erro! Não foi possível atualizar"
        else: 
            self.lblmsg["text"] = "Erro! Babá não encontrada para atualização"
       
        self.txtidbabasitter.delete(0, END)
        self.txtdatagendada.delete(0, END)
        self.txtdataultimotrabalho.delete(0, END)
        self.txtdataatendimento.delete(0, END)

# excluir OK
    def excluirBaba_Sitter(self):
        idbabasitter = self.txtidbabasitter.get()
        datagendada = self.txtdatagendada.get()
        dataultimotrabalho = self.txtdataultimotrabalho.get()
        dataatendimento = self.txtdataatendimento.get()
        resultado = deletarBaby_Sitter(idbabasitter, datagendada)
        if (resultado == True):
            self.lblmsg["text"] = "Dado(s) deletado!"
        else:
            self.lblmsg["text"] = "Erro! Não houve exclusão! babá pode não está cadastrada"
       
        self.txtidbabasitter.delete(0, END)
        self.txtdatagendada.delete(0, END)

# consultar OK
    def buscarBaba_Sitter(self):
        idbabasitter = self.txtidbabasitter.get()
        datagendada = self.txtdatagendada.get()
        dataultimotrabalho = self.txtdataultimotrabalho.get()
        dataatendimento = self.txtdataatendimento.get()
        resultado = consultarBaby_Sitter(idbabasitter, datagendada)
        if (resultado != None):
            self.lblmsg["text"] = resultado
        else:
            self.lblmsg["text"] = "Babá não encontrada!"
       
        self.txtidbabasitter.delete(0, END)
        self.txtdatagendada.delete(0, END)

'''
root = Tk()
root.wm_title("Gerenciamento de Babas")
ApplicationBaby_Sitter(root)
root.mainloop()
'''
