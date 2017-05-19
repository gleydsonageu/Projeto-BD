# -*- coding: utf-8 -*-

from geren_babas import *
from Tkinter import *

class ApplicationMatGasto:
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
        
        self.titulo = Label(self.container1, text="Opções para Material Gasto:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()
        
        self.lblidmaterial = Label(self.container2, text="ID Material Gasto:", font=self.fonte, width=15)
        self.lblidmaterial.pack(side=LEFT)
        
        self.txtidmatgastotextvariable = StringVar(self.container2)
        self.txtidmatgastotextvariable.trace("w", lambda name, index, mode: self.charLimiter(self.txtidmatgastotextvariable))
        
        self.txtidmatgasto = Entry(self.container2, width=30, textvariable=self.txtidmatgastotextvariable)  
        self.txtidmatgasto["width"] = 11
        self.txtidmatgasto["font"] = self.fonte
        self.txtidmatgasto.pack(side=LEFT)
        
        
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarMatGasto
        self.btnBuscar.pack(side=RIGHT)
        
        self.lbldatagendada = Label(self.container3, text="Data Agendada:", font=self.fonte, width=14)
        self.lbldatagendada.pack(side=LEFT)
        
        self.txtdatagendadatextvariable = StringVar(self.container3)
        self.txtdatagendadatextvariable.trace("w", lambda name, index, mode: self.charLimiter2(self.txtdatagendadatextvariable))
   
        self.txtdatagendada = Entry(self.container3, width=30, textvariable=self.txtdatagendadatextvariable)
        self.txtdatagendada["width"] = 40
        self.txtdatagendada["font"] = self.fonte
        self.txtdatagendada.pack(side=LEFT)
   
        self.lblcodmaterial = Label(self.container4, text="Código do Material:", font=self.fonte, width=16)
        self.lblcodmaterial.pack(side=LEFT)
   
        self.txtcodmaterialtextvariable = StringVar(self.container4)
        self.txtcodmaterialtextvariable.trace("w", lambda name, index, mode: self.charLimiter(self.txtcodmaterialtextvariable))
        
        self.txtcodmaterial = Entry(self.container4, width=30, textvariable=self.txtcodmaterialtextvariable)
        self.txtcodmaterial["width"] = 40
        self.txtcodmaterial["font"] = self.fonte
        self.txtcodmaterial.pack(side=LEFT)
   
        self.lblquantidade= Label(self.container5, text="Quantidade:", font=self.fonte, width=10)
        self.lblquantidade.pack(side=LEFT)
        
        self.txtquantidadetextvariable = StringVar(self.container5)
        self.txtquantidadetextvariable.trace("w", lambda name, index, mode: self.charLimiter3(self.txtquantidadetextvariable))
   
        self.txtquantidade = Entry(self.container5, width=30, textvariable=self.txtquantidadetextvariable)
        self.txtquantidade["width"] = 40
        self.txtquantidade["font"] = self.fonte
        self.txtquantidade.pack(side=LEFT)
   
        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirMatGasto
        self.bntInsert.pack (side=LEFT)
   
        self.bntAlterar = Button(self.container8, text="Atualizar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarMatGasto
        self.bntAlterar.pack (side=LEFT)
   
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirMatGasto
        self.bntExcluir.pack(side=LEFT)
   
        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
        

    def charLimiter(self, text):
        text.set(text.get()[0:3])
        
    def charLimiter2(self, text):
        text.set(text.get()[0:10])
        
    def charLimiter3(self, text):
        text.set(text.get()[0:4])    

    def inserirMatGasto(self):
        
        matgasto = Material_Gasto(self.txtidmatgasto.get(), self.txtdatagendada.get(), self.txtcodmaterial.get(), self.txtquantidade.get())
        
        sucesso = criarMaterial_Gasto(matgasto)
        
        if (sucesso == True):
            self.lblmsg["text"] = "Material gasto cadastrado!"
        else:
            self.lblmsg["text"] = "Erro! Não foi possível cadastrar material gasto!"
        
        self.txtidmatgasto.delete(0, END)
        self.txtdatagendada.delete(0, END)
        self.txtcodmaterial.delete(0, END)
        self.txtquantidade.delete(0, END)
        
    def alterarMatGasto(self):
        matgasto = consultarMateria_Gasto(self.txtidmatgasto.get(), self.txtdatagendada.get(),self.txtcodmaterial.get())
        if (matgasto != None):
            quantidade = self.txtquantidade.get()
            if (quantidade != None and quantidade != ""):
                matgasto.quantidade = quantidade
            alt = atualizarMaterial_Gasto(matgasto.id, matgasto.data_agendada, matgasto.cod_material, matgasto)
            if (alt == True):
                self.lblmsg["text"] = "Dado(s) atualizados!"
            else:
                self.lblmsg["text"] = "Erro! Não foi possível atualizar"
        else: 
            self.lblmsg["text"] = "Erro! Material gasto não encontrado para atualização"
       
        self.txtidmatgasto.delete(0, END)
        self.txtdatagendada.delete(0, END)
        self.txtcodmaterial.delete(0, END)
        self.txtquantidade.delete(0, END)
     
    def excluirMatGasto(self):
       
        idmatgasto = self.txtidmatgasto.get()
        datamatgasto = self.txtdatagendada.get()
        codmatgasto = self.txtcodmaterial.get()
        resultado = deletarMaterial_Gasto(idmatgasto, datamatgasto, codmatgasto)
        if (resultado == True):
            self.lblmsg["text"] = "Material gasto Deletado!"
        else:
            self.lblmsg["text"] = "Erro! Não houve exclusão! Material gasto pode não está cadastrado"
       
        self.txtidmatgasto.delete(0, END)
        self.txtdatagendada.delete(0, END)
        self.txtcodmaterial.delete(0, END)      
       
    def buscarMatGasto(self):
       
        idmatgasto = self.txtidmatgasto.get()
        datamatgasto = self.txtdatagendada.get()
        codmatgasto = self.txtcodmaterial.get()
        resultado = consultarMateria_Gasto(idmatgasto, datamatgasto, codmatgasto)
        if (resultado != None):
            self.lblmsg["text"] = resultado
        else:
            self.lblmsg["text"] = "Material gasto não encontrado!"
       
        self.txtidmatgasto.delete(0, END)
        self.txtdatagendada.delete(0, END)
        self.txtcodmaterial.delete(0, END)              
'''     
root = Tk()
root.wm_title("Gerenciamento de Babas")
ApplicationMatGasto(root)
root.mainloop()
'''    
