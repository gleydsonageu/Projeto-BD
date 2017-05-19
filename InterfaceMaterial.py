# -*- coding: utf-8 -*

from geren_babas import *
from Tkinter import *

class ApplicationMaterial:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        
        self.tituloMaterial = Frame(master)
        self.tituloMaterial["pady"] = 10
        self.tituloMaterial.pack()
        self.containerCod_material = Frame(master)
        self.containerCod_material["padx"] = 20
        self.containerCod_material["pady"] = 5
        self.containerCod_material.pack()
        self.containerDescricao = Frame(master)
        self.containerDescricao["padx"] = 20
        self.containerDescricao["pady"] = 5
        self.containerDescricao.pack()
        self.containerbotao = Frame(master)
        self.containerbotao["padx"] = 20
        self.containerbotao["pady"] = 10
        self.containerbotao.pack()
        self.containertexto = Frame(master)
        self.containertexto["pady"] = 15
        self.containertexto.pack()

        self.titulo = Label(self.tituloMaterial, text="Opções para material:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblcod_material = Label(self.containerCod_material, text="código material:", font=self.fonte, width=16)
        self.lblcod_material.pack(side=LEFT)

        self.txtcodigomaterialvariable = StringVar(self.containerCod_material)
        self.txtcodigomaterialvariable.trace("w", lambda name, index, mode: self.charLimiter(self.txtcodigomaterialvariable))

        self.txtcodmaterial = Entry(self.containerCod_material, width = 4, textvariable=self.txtcodigomaterialvariable)
        self.txtcodmaterial["font"] = self.fonte
        self.txtcodmaterial.pack(side=LEFT)

        self.btnBuscar = Button(self.containerCod_material, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarMaterial
        self.btnBuscar.pack(side=RIGHT)

        self.ldldescricao_mat = Label(self.containerDescricao, text="Descrição:", font=self.fonte, width=10)
        self.ldldescricao_mat.pack(side=LEFT)

        self.txtdescricaovariable = StringVar(self.containerDescricao)
        self.txtdescricaovariable.trace("w", lambda name, index, mode: self.charLimiter2(self.txtdescricaovariable))

        self.txtdescricao_mat = Entry(self.containerDescricao, width = 30, textvariable=self.txtdescricaovariable)
        self.txtdescricao_mat["width"] = 40
        self.txtdescricao_mat["font"] = self.fonte
        self.txtdescricao_mat.pack(side=LEFT)

        self.bntInsert = Button(self.containerbotao, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirMaterial
        self.bntInsert.pack (side=LEFT)
   
        self.bntAlterar = Button(self.containerbotao, text="Atualizar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarMaterial
        self.bntAlterar.pack (side=LEFT)
   
        self.bntExcluir = Button(self.containerbotao, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirMaterial
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.containertexto, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
   
    def charLimiter(self, text):
            text.set(text.get()[0:4])

    def charLimiter2(self, text):
            text.set(text.get()[0:80])


    def inserirMaterial(self):
            
        material = Material(self.txtcodmaterial.get(), self.txtdescricao_mat.get())
        
        sucesso = criarMaterial(material)
        
        if (sucesso == True):
            self.lblmsg["text"] = "Material criado!"
        else:
            self.lblmsg["text"] = "Erro! Não foi possivel cadastrar o Material!"
        
        self.txtcodmaterial.delete(0, END)
        self.txtdescricao_mat.delete(0, END)

    def alterarMaterial(self):
        material = consultarMaterial(self.txtcodmaterial.get())
        if (material != None):
            descricao = self.txtdescricao_mat.get()
            if (descricao != None and descricao != ""):
                material.descricao = descricao
                
            alt = atualizarMaterial(material.cod_material, material)
            if (alt == True):
                self.lblmsg["text"] = "Dado(s) atualizados!"
            else:
                self.lblmsg["text"] = "Erro! Não foi possível atualizar"
        else: 
            self.lblmsg["text"] = "Erro! Material não encontrado para a atualização"
       
        self.txtcodmaterial.delete(0, END)
        self.txtdescricao_mat.delete(0, END)

    def excluirMaterial(self):
            
        codmaterial = self.txtcodmaterial.get()
        resultado = deletarMaterial(codmaterial)
        if(resultado == True):
            self.lblmsg["text"] = "Material Deletado!"
        else:
            self.lblmsg["text"] = "Erro! Não houve exclusão, material não está cadastrado"

        self.txtcodmaterial.delete(0, END) 

    def buscarMaterial(self):
        
        codmaterial = self.txtcodmaterial.get()
        resultado = consultarMaterial(codmaterial)
        if (resultado != None):
            self.lblmsg["text"] = resultado
        else:
            self.lblmsg["text"] = "Material não encontrado!"

        self.txtcodmaterial.delete(0, END)
'''
root = Tk()
ApplicationMaterial(root)
root.wm_title("Gerenciamendo de Material")
root.mainloop()
'''
