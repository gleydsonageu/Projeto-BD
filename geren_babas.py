# -*- coding: utf-8 -*-

import mysql.connector
from datetime import date, datetime, timedelta
cnx = mysql.connector.connect(user='root', password='110389', host='127.0.0.1', database='babas_sob_demanda')

class Cliente:
    def __init__(self, cpf, nome_cli, telefone, email):
        self.cpf = cpf
        self.nome_cli = nome_cli
        self.telefone = telefone
        self.email = email
        
    def __str__(self):
        return "CPF: %s, Nome: %s, Telefone: %s, Email: %s" % (self.cpf, self.nome_cli, self.telefone, self.email) 
        
def criarCliente(cliente):
    try:
        cursor = cnx.cursor()
        inserir = "insert into Cliente(cpf, nome_cli, telefone, email) values (%s,%s,%s,%s)"
        dados = [cliente.cpf, cliente.nome_cli, cliente.telefone, cliente.email]
        cursor.execute(inserir, dados)
        cnx.commit()
        cursor.close()
        return True
    except:
        return False    

def deletarCliente(cpf):
    try:
        cursor = cnx.cursor()
        remover = "delete from Cliente where cpf = %s;"
        dados = [cpf]
        cursor.execute(remover, dados)
        cnx.commit()
        deleted_row_count = cursor.rowcount
        cursor.close()
        if deleted_row_count == 1:
            return True
        else:
            return False
    except:
        return False

def consultarCliente(cpf):
    cursor = cnx.cursor()
    consulta = "select * from Cliente where cpf = %s"
    dados = [cpf]
    cursor.execute(consulta, dados)
    resultados = list(cursor)
    cursor.close()
    
    if (len(resultados) == 0):
        print "Cliente não existe!"
        return None
    else:
        dados_cliente = resultados[0]
        cliente = Cliente(dados_cliente[0], dados_cliente[1], dados_cliente[2], dados_cliente[3])
        print cliente
        return cliente
    
def atualizarCliente(cpf, cliente):
    try:
        cursor = cnx.cursor()
        atualizacao = "update Cliente set nome_cli = %s, telefone = %s, email = %s where cpf = %s"
        dados = [cliente.nome_cli, cliente.telefone, cliente.email, cpf]
        cursor.execute(atualizacao, dados)
        cnx.commit()
        deleted_row_count = cursor.rowcount
        cursor.close()
        if deleted_row_count == 1:
            return True
        else:
            return False
    except:
        return False
        
    
class Crianca:
    def __init__(self, id, nome, idade, cpf):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def __str__(self):
        return "ID: %s, Nome: %s, idade: %s, CPF: %s" % (self.id, self.nome, self.idade, self.cpf) 
        
def criarCrianca(crianca):
    try:
        cursor = cnx.cursor()
        inserir = "insert into Crianca(id, nome, idade, cpf) values (%s,%s,%s,%s)"
        dados = [crianca.id, crianca.nome, crianca.idade, crianca.cpf]
        cursor.execute(inserir, dados)
        cnx.commit()
        cursor.close()
        return True
    except:
        return False

def deletarCrianca(id):
    try:
        cursor = cnx.cursor()
        remover = "delete from Crianca where id = %s;"
        dados = [id]
        cursor.execute(remover, dados)
        cnx.commit()
        deleted_row_count = cursor.rowcount
        cursor.close()
        if deleted_row_count == 1:
            return True
        else:
            return False
    except:
        return False
    
def consultarCrianca(id):
    cursor = cnx.cursor()
    consulta = "select * from Crianca where id = %s"
    dados = [id]
    cursor.execute(consulta, dados)
    resultados = list(cursor)
    cursor.close()
    
    if (len(resultados) == 0):
        print "Crianca não existe!"
        return None
    else:
        dados_crianca = resultados[0]
        crianca = Crianca(dados_crianca[0], dados_crianca[1], dados_crianca[2], dados_crianca[3])
        print crianca
        return crianca
    
def atualizarCrianca(id, crianca):
    try:
        cursor = cnx.cursor()
        atualizacao = "update Crianca set nome = %s, idade = %s, cpf = %s where id = %s"
        dados = [crianca.nome, crianca.idade, crianca.cpf, id]
        cursor.execute(atualizacao, dados)
        cnx.commit()
        deleted_row_count = cursor.rowcount
        cursor.close()
        if deleted_row_count == 1:
            return True
        else:
            return False
    except:
        return False
    
class Baby_Sitter:
    def __init__(self, id, data_agendada, data_ultimo_trabalho, data_atendimento):
        self.id = id
        self.data_agendada = data_agendada
        self.data_ultimo_trabalho = data_ultimo_trabalho
        self.data_atendimento = data_atendimento

    def __str__(self):
        return "ID: %s, data_agendada: %s, data_ultimo_trabalho: %s, data_atendimento: %s" % (self.id, self.data_agendada, self.data_ultimo_trabalho, self.data_atendimento)

def criarBaby_Sitter(baby_sitter):
    try:
        cursor = cnx.cursor()
        inserir = "insert into Baby_Sitter(id, data_agendada, data_ultimo_trabalho, data_atendimento) values (%s,%s,%s,%s)"
        dados = [baby_sitter.id, baby_sitter.data_agendada, baby_sitter.data_ultimo_trabalho, baby_sitter.data_atendimento]
        cursor.execute(inserir, dados)
        cnx.commit()
        cursor.close()
        return True
    except:
        return False 

def deletarBaby_Sitter(id, data_agendada):
    try:
        cursor = cnx.cursor()
        remover = "delete from Baby_Sitter where id = %s AND data_agendada = %s;"
        dados = [id, data_agendada]
        cursor.execute(remover, dados)
        cnx.commit()
        deleted_row_count = cursor.rowcount
        cursor.close()
        if deleted_row_count ==1:
            return True
        else:
            return False
    except:
        return False

def consultarBaby_Sitter(id, data_agendada):
    cursor = cnx.cursor()
    consulta = "select * from Baby_Sitter where id = %s AND data_agendada = %s"
    dados = [id, data_agendada]
    cursor.execute(consulta, dados)
    resultados = list(cursor)
    cursor.close()

    if (len(resultados) == 0):
        print "Não existe está babá agendada"
        return None
    else:
        dados_baby_sitter = resultados[0]
        baby_sitter = Baby_Sitter(dados_baby_sitter[0], dados_baby_sitter[1], dados_baby_sitter[2], dados_baby_sitter[3])
        print baby_sitter
        return baby_sitter

def atualizarBaby_Sitter(id, data_agendada, baby_sitter):
    try:
        cursor = cnx.cursor()
        atualizacao = "update Baby_Sitter set data_ultimo_trabalho = %s, data_atendimento = %s where id = %s AND data_agendada = %s"
        dados = [baby_sitter.data_ultimo_trabalho, baby_sitter.data_atendimento, id, data_agendada]
        cursor.execute(atualizacao,dados)
        cnx.commit()
        deleted_row_count = cursor.rowcount
        cursor.close()
        if deleted_row_count == 1:
          return True
        else:
           return False
    except:
        return False
    
class Material:
    def __init__(self, cod_material, descricao):
        self.cod_material = cod_material
        self.descricao = descricao

    def __str__(self):
        return "cod_material: %s, descricao: %s" % (self.cod_material, self.descricao)
        
def criarMaterial(material):
    try:
        cursor = cnx.cursor()
        inserir = "insert into Material(cod_material, descricao) values (%s,%s)"
        dados = [material.cod_material, material.descricao]
        cursor.execute(inserir, dados)
        cnx.commit()
        cursor.close()
        return True
    except:
        return False

def deletarMaterial(cod_material):
    try:
        cursor = cnx.cursor()
        remover = "delete from Material where cod_material = %s;"
        dados = [cod_material]
        cursor.execute(remover,dados)
        cnx.commit()
        deleted_row_count = cursor.rowcount
        cursor.close()
        if deleted_row_count == 1:
            return True
        else:
            return False
    except:
        return False

def consultarMaterial(cod_material):
    cursor = cnx.cursor()
    consulta = "select * from Material where cod_material = %s"
    dados = [cod_material]
    cursor.execute(consulta, dados)
    resultados = list(cursor)
    cursor.close()

    if (len(resultados) == 0):
        print "Material não existe!"
        return None
    else:
        dados_material = resultados[0]
        material = Material(dados_material[0], dados_material[1])
        print material
        return material

def atualizarMaterial(cod_material, material):
    try:
        cursor = cnx.cursor()
        atualizacao = "update Material set descricao = %s where cod_material = %s"
        dados = [material.descricao, cod_material]
        cursor.execute(atualizacao, dados)
        cnx.commit()
        deleted_row_count = cursor.rowcount
        cursor.close()
        if deleted_row_count == 1:
            return True
        else:
            return False
    except:
        return False
    
class Material_Gasto:
    def __init__(self, id, data_agendada, cod_material, quantidade):
        self.id = id
        self.data_agendada = data_agendada
        self.cod_material = cod_material
        self.quantidade = quantidade

    def __str__(self):
        return "ID: %s, data_agendada: %s, cod_material: %s, quantidade: %s" % (self.id, self.data_agendada, self.cod_material, self.quantidade)

def criarMaterial_Gasto(material_gasto):
        try:
            cursor = cnx.cursor()
            inserir = "insert into Material_Gasto(id, data_agendada, cod_material, quantidade) values (%s,%s,%s,%s)"
            dados = [material_gasto.id, material_gasto.data_agendada, material_gasto.cod_material, material_gasto.quantidade]
            cursor.execute(inserir, dados)
            cnx.commit()
            cursor.close()
            return True
        except:
            return False
        
        
def deletarMaterial_Gasto(id, data_agendada, cod_material):
    try:
        cursor = cnx.cursor()
        remover = "delete from Material_Gasto where id = %s AND data_agendada = %s AND cod_material = %s;"
        dados = [id, data_agendada, cod_material]
        cursor.execute(remover, dados)
        cnx.commit()
        deleted_row_count = cursor.rowcount
        cursor.close()
        if deleted_row_count == 1:
            return True
        else:
            return False
    except:
        return False

def consultarMateria_Gasto(id, data_agendada, cod_material):
    cursor = cnx.cursor()
    consulta = "select * from Material_Gasto where id = %s AND data_agendada = %s AND cod_material = %s"
    dados = [id, data_agendada, cod_material]
    cursor.execute(consulta, dados)
    resultados = list(cursor)
    cursor.close()

    if (len(resultados) == 0):
        print "Não há material gasto com este id"
        return None
    else:
        dados_material_gasto = resultados[0]
        material_gasto = Material_Gasto(dados_material_gasto[0], dados_material_gasto[1], dados_material_gasto[2], dados_material_gasto[3])
        print material_gasto
        return material_gasto

def atualizarMaterial_Gasto(id,data_agendada, cod_material, material_gasto):
    try:
        cursor = cnx.cursor()
        atualizacao = "update Material_Gasto set quantidade = %s where id = %s AND data_agendada = %s AND cod_material = %s"
        dados =[material_gasto.quantidade, id, data_agendada, cod_material]
        cursor.execute(atualizacao,dados)
        cnx.commit()
        deleted_row_count = cursor.rowcount
        cursor.close()
        return True
    except:
        return False
        

    
#cliente = consultarCliente("88888888888")
#cliente.nome_cli = 'sara'
#atualizarCliente('88888888888', cliente)  
#crianca = consultarCrianca(147)
#crianca.idade = 4 
#atualizarCrianca(147, crianca) 

#deletarCliente("88888888888")

#cliente = Cliente("44444444444", "Fatima", "8177777777", "fatima@email.com")
#criarCliente(cliente)

#matg = Material_Gasto(147,"2017-01-24", 222, 24)
#print matg
#criarMaterial_Gasto(matg)

#consu = consultarMateria_Gasto(123, '2017-02-01', 666)
#consu.quantidade = 30
#atualizarMaterial_Gasto(123, "2017-02-01", 666, consu)

#deletarMaterial_Gasto(123, '2017-02-01', 666)


 
