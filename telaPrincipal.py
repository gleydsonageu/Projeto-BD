# -*- coding: utf-8 -*
from Tkinter import *
from Interface import *
from InterfaceCrianca import *
from InterfaceMaterial import *
from InterfaceMaterialGasto import *
from InterfaceBaby_Sitter import *

class TelaPrincipal():
    def __init__(self, master=None):
        self.fonte = ("Verdana", "10")

        self.tituloJanela = Frame(master)
        self.tituloJanela["pady"] = 10
        self.tituloJanela.pack()
        self.containerBaba = Frame(master)
        self.containerBaba["padx"] = 20
        self.containerBaba["pady"] = 5
        self.containerBaba.pack()
        self.containerCrianca = Frame(master)
        self.containerCrianca["padx"] = 20
        self.containerCrianca["pady"] = 5
        self.containerCrianca.pack()
        self.containerCliente = Frame(master)
        self.containerCliente["padx"] = 20
        self.containerCliente["pady"] = 5
        self.containerCliente.pack()
        self.containerMaterial = Frame(master)
        self.containerMaterial["padx"] = 20
        self.containerMaterial["pady"] = 5
        self.containerMaterial.pack()
        self.containerMaterialGasto = Frame(master)
        self.containerMaterialGasto["padx"] = 20
        self.containerMaterialGasto["pady"] = 5
        self.containerMaterialGasto.pack()

        self.tituloJanela = Label(self.tituloJanela, text="Selecione o conteúdo desejado")
        self.tituloJanela["font"] = ("Calibri", "15", "bold")
        self.tituloJanela.pack()

        self.root = None
        self.bntBaba = Button(self.containerBaba, text="Babá", font=self.fonte, width=12)
        self.bntBaba["command"] = self.new_janBaby_Sitter
        self.bntBaba.pack(side=LEFT)

        self.root = None
        self.bntCrianca = Button(self.containerCrianca, text="Criança", font=self.fonte, width=12)
        self.bntCrianca["command"] = self.new_janCrianca
        self.bntCrianca.pack(side=LEFT)

        self.root = None
        self.bntCliente = Button(self.containerCliente, text="Cliente", font=self.fonte, width=12)
        self.bntCliente["command"] = self.new_janCliente
        self.bntCliente.pack(side=LEFT)

        self.root = None
        self.bntMaterial = Button(self.containerMaterial, text="Material", font=self.fonte, width=12)
        self.bntMaterial["command"] = self.new_janMaterial
        self.bntMaterial.pack(side=LEFT)        

        self.root = None
        self.bntMaterialGasto = Button(self.containerMaterialGasto, text="Material Gasto", font=self.fonte, width=12)
        self.bntMaterialGasto["command"] = self.new_janMatGasto
        self.bntMaterialGasto.pack(side=LEFT)                


    def new_janCliente(self):
        # Verifica se já foi criada
        if self.root is None:
           self.root = Tk()
           Application(self.root)
           self.root.wm_title("Gerenciamento de baba")
           self.root.protocol("WM_DELETE_WINDOW", self.fecha_janCliente)
        else:
            # Se já foi, basta colocá-la na frente
            self.root.lift()

    def fecha_janCliente(self):
        # Seta de novo em None para recriar quando abrir
        self.root.destroy()
        self.root = None
        
    def new_janCrianca(self):
        # Verifica se já foi criada
        if self.root is None:
           self.root = Tk()
           ApplicationCrianca(self.root)
           self.root.wm_title("Gerenciamento de babas")
           self.root.protocol("WM_DELETE_WINDOW", self.fecha_janCrianca)
        else:
            # Se já foi, basta colocá-la na frente
            self.root.lift()

    def fecha_janCrianca(self):
        # Seta de novo em None para recriar quando abrir
        self.root.destroy()
        self.root = None
        
    def new_janMaterial(self):
        if self.root is None:
           self.root = Tk()
           ApplicationMaterial(self.root)
           self.root.wm_title("Gerenciamento de babas")
           self.root.protocol("WM_DELETE_WINDOW", self.fecha_janMaterial)
        else:
            self.root.lift()

    def fecha_janMaterial(self):
        self.root.destroy()
        self.root = None
        
    def new_janMatGasto(self):
        # Verifica se já foi criada
        if self.root is None:
           self.root = Tk()
           ApplicationMatGasto(self.root)
           self.root.wm_title("Gerenciamento de babas")
           self.root.protocol("WM_DELETE_WINDOW", self.fecha_janMatGasto)
        else:
            # Se já foi, basta colocá-la na frente
            self.root.lift()

    def fecha_janMatGasto(self):
        # Seta de novo em None para recriar quando abrir
        self.root.destroy()
        self.root = None
        
    def new_janBaby_Sitter(self):
        if self.root is None:
           root = Tk()
           root.wm_title("Gerenciamento de Babas")
           ApplicationBaby_Sitter(root)
           root.mainloop()
           self.root.protocol("WM_DELETE_WINDOW", self.fecha_janBaby_Sitter)
        else:
            self.root.lift()

    def fecha_janBaby_Sitter(self):
        self.root.destroy()
        self.root = None
        
        
root = Tk()
TelaPrincipal(root)
root.wm_title("Gerenciamento de Babas")
root.mainloop()
