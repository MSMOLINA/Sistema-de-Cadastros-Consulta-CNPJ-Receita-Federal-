import sqlite3


class Data_base:

    def __init__(self, name = 'system.db') -> None:
        
        self.name = name
       
    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_company(self):

        cursor = self.connection.cursor()
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Empresas(

            CNPJ TEXT,
            NOME TEXT,
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            UF TEXT,
            CEP TEXT,
            TELEFONE TEXT,
            EMAIL TEXT,
            CONTRATO TEXT, 
            SISTEMA TEXT,
            HORAS TEXT,
            ASSISTENCIA TEXT,
            INICIO_CONTRATO TEXT,
            FIM_CONTRATO TEXT,
            RESP_CONSULTORIA TEXT,
            EMAIL_RESP_CONSULTORIA TEXT,
            TEL_RESP_CONSULTORIA TEXT,
            CARGO_RESP_CONSULTORIA TEXT,

            PRIMARY KEY(CNPJ)        
            );  

        """)

    def register_company(self, fullDataSet):

        campos_tabela = ('CNPJ','NOME','LOGRADOURO','NUMERO','COMPLEMENTO','BAIRRO','MUNICIPIO',
        'UF','CEP','TELEFONE','EMAIL','CONTRATO','SISTEMA','HORAS','ASSISTENCIA','INICIO_CONTRATO','FIM_CONTRATO',
        'RESP_CONSULTORIA','EMAIL_RESP_CONSULTORIA','TEL_RESP_CONSULTORIA','CARGO_RESP_CONSULTORIA')

        qntd = ("?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?")       
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Empresas {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return("OK")

        except:
            return "Erro"

    #Método para Selecionar os dados que serão exibidos na tabela
    def select_all_companies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Empresas ORDER BY NOME")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass

    def delete_companies(self, id):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Empresas WHERE CNPJ = '{id}' ") 

            self.connection.commit()

            return "Cadastro de empresa excluído com Sucesso!"
        
        except:
            return "Erro ao Excluir o Registro!"

    def update_company(self, fullDataSet):

        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE Empresas set

            CNPJ = '{fullDataSet[0]}',
            NOME = '{fullDataSet[1]}',
            LOGRADOURO = '{fullDataSet[2]}',
            NUMERO =  '{fullDataSet[3]}',
            COMPLEMENTO =  '{fullDataSet[4]}',
            BAIRRO = '{fullDataSet[5]}',
            MUNICIPIO = '{fullDataSet[6]}',
            UF = '{fullDataSet[7]}',
            CEP = '{fullDataSet[8]}',
            TELEFONE = '{fullDataSet[9]}',
            EMAIL = '{fullDataSet[10]}',
            CONTRATO = '{fullDataSet[11]}',
            SISTEMA = '{fullDataSet[12]}',
            HORAS = '{fullDataSet[13]}',
            ASSISTENCIA = '{fullDataSet[14]}',
            INICIO_CONTRATO = '{fullDataSet[15]}',
            FIM_CONTRATO = '{fullDataSet[16]}',
            RESP_CONSULTORIA = '{fullDataSet[17]}',
            EMAIL_RESP_CONSULTORIA = '{fullDataSet[18]}',
            TEL_RESP_CONSULTORIA = '{fullDataSet[19]}',
            CARGO_RESP_CONSULTORIA = '{fullDataSet[20]}'

            WHERE CNPJ = '{fullDataSet[0]}'""")
        self.connection.commit()        

    
