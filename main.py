# -*- coding: utf-8 -*-
from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon 
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QComboBox)
from ui_main import Ui_MainWindow
from ui_functions import *
from database import Data_base
import pandas as pd
import sqlite3
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Py_MMDesenvolvimento - Sistema de Cadastros de Empresas")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        # Função para Toggle Button ------------------------------------------------------
        self.btn_toggle.clicked.connect(self.leftMenu)
        #---------------------------------------------------------------------------------

        #Páginas do Sistema ---------------------------------------------------------------
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastrar))
        self.btn_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        #-----------------------------------------------------------------------------------

        #Preencher automaticamente os dados do CNPJ-----------------------------------------
        self.txt_cnpj.editingFinished.connect(self.consulta_api)

        self.pushButton_5.clicked.connect(self.cadastrar_empresas) #Comando Gravar informações no banco de dados "Botão Cadastrar"
        self.btn_alterar.clicked.connect(self.update_company)
        self.btn_excluir.clicked.connect(self.deletar_empresas)
        self.btn_excel.clicked.connect(self.gerar_excel)
        

        self.buscar_empresas()

    #Função para configuração do Menu
    def leftMenu(self):
    
        width = self.left_menu.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animation.setDuration(200)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    #Consultar API Receita Federal
    def consulta_api(self):
        campos = consulta_cnpj(self.txt_cnpj.text())

        self.txt_nome.setText(campos[0])
        self.txt_logradouro.setText(campos[1])
        self.txt_numero.setText(campos[2])
        self.txt_complemento.setText(campos[3])
        self.txt_bairro.setText(campos[4])
        self.txt_municipio.setText(campos[5])
        self.txt_uf.setText(campos[6])
        self.txt_cep.setText(campos[7].replace('.', '').replace('-', ''))
        self.txt_telefone.setText(campos[8].replace('(', '').replace('-', '').replace(')', ''))
        self.txt_email.setText(campos[9])
        

    def cadastrar_empresas(self):   
        db = Data_base()
        db.connect()

        fullDataSet = (
            self.txt_cnpj.text(),
            self.txt_nome.text(),
            self.txt_logradouro.text(),
            self.txt_numero.text(),
            self.txt_complemento.text(),
            self.txt_bairro.text(),
            self.txt_municipio.text(),
            self.txt_uf.text(),
            self.txt_cep.text(),
            self.txt_telefone.text().strip(),
            self.txt_email.text(),
            self.txt_Num_Cont.text(),
            self.txt_sistema.text(),
            self.txt_hs_contrato.text(),
            self.txt_tp_assistencia.text(),
            self.txt_inicio_contrato.text(),
            self.txt_fim_contrato_2.text(),
            self.txt_resp_cons.text(),
            self.txt_resp_email_cons.text(),
            self.txt_tel_resp_cons.text(),
            self.txt_resp_cargo.text(),
        )

                      
    #Cadastrar as informações no Banco de Dados----------------------------------------------
        resp = db.register_company(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro Realizado com Sucesso!")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidas corretamente! ")
            msg.exec()
            db.close_connection()
            return

               

    
    def buscar_empresas(self):

        db = Data_base()
        db.connect()
        result = db.select_all_companies()

        self.tb_company.clearContents()
        self.tb_company.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_company.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connection()

    def update_company(self):

        dados = []
        update_dados = []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
            update_dados.append(dados)
            dados = []

        #Atualizar dados no banco
        db = Data_base()
        db.connect()

        for emp in update_dados:
            db.update_company(tuple(emp))
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()

        self.tb_company.reset()
        self.buscar_empresas()    

    def deletar_empresas(self):

        db = Data_base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este Registro será Excluído.")
        msg.setInformativeText("Você tem Certeza que Deseja Excluir o Registro?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cnpj = self.tb_company.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_companies(cnpj)
            self.buscar_empresas()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EMPRESAS")
            msg.setText(result)
            msg.exec()


        db.close_connection()

    def gerar_excel(self):
        
        dados = []
        all_dados = []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['CNPJ','NOME','LOGRADOURO','NUMERO','COMPLEMENTO',
            'BAIRRO','MUNICIPIO','UF','CEP','TELEFONE','EMAIL','CONTRATO','SISTEMA','HORAS',
            'ASSISTENCIA','INICIO_CONTRATO','FIM_CONTRATO','RESP_CONSULTORIA','EMAIL_RESP_CONSULTORIA',
            'TEL_RESP_CONSULTORIA','CARGO_RESP_CONSULTORIA']

        empresas = pd.DataFrame(all_dados, columns= columns)
        empresas.to_excel("Relação Empresas.xlsx", sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel Gerado com Sucesso!")
        msg.exec()

    def extrair_dados_excel_banco():

        conexao = sqlite3.connect("system.db")

        empresas = pd.read_sql_query("""SELECT * FROM Empresas""", conexao)

        empresas.to_excel("Relação Empresas.xlsx", sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel Gerado com Sucesso!")
        msg.exec()

    
if __name__ == "__main__":

    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()