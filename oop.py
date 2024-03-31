import pandas as pd
from sys import exit 
from time import sleep
import os
from tkinter import filedialog, Tk
from openpyxl import Workbook

#rodar loop do tk
root = Tk()
root.withdraw()


###parte visual###
cor_vermelha = '\033[31m'
cor_amarela = '\033[33m'
cor_branca = '\033[97m'
fundo_vermelho = '\033[41m'
cor_verde = '\033[32m'
restaurar_cor = '\033[0m'
cor_azul = '\033[34m'

def carregar():
    carregar = "Carregando"
    for letra in carregar:
        sleep(0.15)
        print(f"{cor_amarela}{letra}{restaurar_cor}",end="",flush=True)
    for i in range(4):
        sleep(0.15)
        print(f"{cor_amarela}.{restaurar_cor}",end="",flush=True)
    print("\n")

def safe_exist_db(dir):
    existent_db = os.path.join(dir, "data_base.xlsx")
    if os.path.exists(existent_db):
        return True
    if not os.path.exists(existent_db):
        return False

def create_db(dir):
        wb = Workbook()
        cliente = wb.active
        cliente.title = "Clientes"
        adm = wb.create_sheet("Administradores")
        cliente["A1"] = "Nome"
        cliente["B1"] = "Data de nascimento"
        cliente["C1"] = "Email"
        cliente["D1"] = "CPF"
        cliente["E1"] = "Senha"
        adm["A1"] = "Nome"
        adm["B1"] = "Data de nascimento"
        adm["C1"] = "Email"
        adm["D1"] = "CPF"
        adm["E1"] = "Senha"
        wb.save(f"{dir}")

def load_db():
    print(f"{cor_amarela}Escolha uma das opções abaixo:{restaurar_cor}")
    print(f"{cor_amarela}(1) {restaurar_cor}", end="")
    print("Criar database no diretório atual.")
    print(f"{cor_amarela}(2) {restaurar_cor}", end="")
    print("Selecionar um diretório para criar o database.")
    print(f"{cor_amarela}(3) {restaurar_cor}", end="")
    print("Selecionar diretório para um database já existente.")
    print(f"{cor_amarela}(4) {restaurar_cor}", end="")
    print("Verificar o diretório selecionado.")

    while True:
        while True:
            try:
                escolha = int(input(f"{cor_amarela}R: {restaurar_cor}"))
                if escolha in range(1,5):
                    break
                else:
                    print(f"{fundo_vermelho}{cor_branca}Por favor escolha uma opção válida!{restaurar_cor}")
                    pass
            except Exception:
                    print(f"{fundo_vermelho}{cor_branca}Por favor escolha um número!{restaurar_cor}")
                    pass
                
        if escolha == 1:
            dir_padrao = os.path.dirname(__file__)
            dir_db = os.path.join(dir_padrao, "data_base.xlsx")
            create_db(dir_db)
            carregar()
            return True, dir_db

        elif escolha == 2:
            dir_personalizado = filedialog.askdirectory()
            while not dir_personalizado:
                print(f"{cor_vermelha}Você não selecionou nenhum diretório{restaurar_cor}")
                print(f"{cor_amarela}Por favor selecione um diretório{restaurar_cor}")
                dir_personalizado = filedialog.askdirectory()
            dir_db = os.path.join(dir_personalizado, "data_base.xlsx")
            safe_db = safe_exist_db(dir_personalizado)
            if safe_db == True:
                print(f"{cor_amarela}Já existe um database no diretório selecionado! Desejesa sobrescrever?\n", 
                      f"{cor_azul}Responda com sim ou não!{restaurar_cor}")
                while True:
                    escolha_safe_exist_db = input(f"{cor_amarela}R: {restaurar_cor}")
                    if escolha_safe_exist_db[0].lower() == "s":
                        create_db(dir_db)
                        carregar()
                        return True, dir_db
                    elif escolha_safe_exist_db[0].lower() == "n":
                        return False, dir_db
                    else:
                        print(f"{cor_vermelha}Selecione uma opção válida!{restaurar_cor}")
                        pass
            else:
                create_db(dir_db)
                carregar()
                return True, dir_db

        elif escolha == 3:
            dir_db_exist = filedialog.askdirectory()
            while not dir_db_exist:
                print(f"{cor_vermelha}Você não selecionou nenhum diretório{restaurar_cor}")
                print(f"{cor_amarela}Por favor selecione um diretório{restaurar_cor}")
                dir_db_exist = filedialog.askdirectory()
            if not os.path.exists(os.path.join(dir_db_exist, "data_base.xlsx")):
                while True:
                    print(f"{cor_vermelha}O diretório: {cor_azul}{dir_db_exist}{restaurar_cor}",
                           f"{cor_vermelha}\nNão contém um database!{restaurar_cor}")
                    print(f"{cor_azul}O que prefere fazer?{restaurar_cor}")
                    print(f"{cor_amarela}(1) {restaurar_cor}", end="")
                    print("Voltar ao menu.")
                    print(f"{cor_amarela}(2) {restaurar_cor}", end="")
                    print("Selecionar diretório novamente.")
                    while True:
                        try:
                            escolha_menu_db_nao_existe = int(input(f"{cor_amarela}R: {restaurar_cor}"))
                            if escolha_menu_db_nao_existe in range(1,3):
                                break
                            else:
                                print(f"{cor_vermelha}Selecione um número válido{restaurar_cor}")
                                pass
                        except Exception:
                            print(f"{cor_branca}{fundo_vermelho}Selecione uma opção válida{restaurar_cor}")
                            pass
                    if escolha_menu_db_nao_existe == 1:
                        return False, None
                    elif escolha_menu_db_nao_existe == 2:
                        dir_db_exist = filedialog.askdirectory()
                        if not os.path.exists(os.path.join(dir_db_exist, "data_base.xlsx")):    
                            continue
                        elif os.path.exists(os.path.join(dir_db_exist, "data_base.xlsx")):
                            dir_db = (os.path.join(dir_db_exist, "data_base.xlsx"))
                            carregar()
                            return True, dir_db
                        else:
                            pass
            elif os.path.exists(os.path.join(dir_db_exist, "data_base.xlsx")):
                dir_db_exist = (os.path.join(dir_db_exist, "data_base.xlsx"))
                carregar()
                return True, dir_db_exist
            else:
                print(f"{cor_branca}{fundo_vermelho}Ocorreu algum erro durante a seleção, por favor tente novamente{restaurar_cor}")
                pass
        elif escolha == 4:
            dir_padrao = os.path.dirname(os.path.abspath(__file__))
            print(f"{cor_amarela}O diretório atual/padrão é:", f"{cor_azul}{dir_padrao}{restaurar_cor}")
            return False, dir_padrao
        else:
            print(f"{cor_branca}{fundo_vermelho}Ocorreu algum erro durante a seleção, por favor tente novamente{restaurar_cor}")
            pass

def init_db():
    while True:
        dir_padrao = os.path.dirname(os.path.abspath(__file__))
        dir_padrao = os.path.join(dir_padrao, "data_base.xlsx")
        print(f'{cor_azul}Procurando banco de dados{restaurar_cor}')
        carregar()
        if os.path.exists(dir_padrao):
            print(f"{cor_verde}Banco de dados encontrado!{restaurar_cor}")
            df = pd.read_excel(dir_padrao)
            return df, dir_padrao
        else:
            print(f'{cor_vermelha}Banco de dados ainda nao foi criado!{restaurar_cor}')
            db_found, dir_db = load_db() 
            if db_found:
                df = pd.read_excel(dir_db)
                print(f"{cor_verde}Banco de dados carregado!{restaurar_cor}")
                return df, dir_db
            elif not db_found:
                while True:
                    db_found, dir_db = load_db()
                    if db_found:
                        df = pd.read_excel(dir_db)
                        print(f"{cor_verde}Banco de dados carregado!{restaurar_cor}")
                        return df, dir_db
                    else:
                        pass

class Cliente():
    def init(self, nome, data_de_nascimento, email, cpf, senha):
        self.nome = nome
        self.nome = data_de_nascimento
        self.email = email
        self.cpf = cpf
        self.senha = senha

    def logar(self):
        email = str(input("Por favor digite seu email: "))
        senha = str(input("Por favor digite sua senha: "))
        if email == self.email and senha == self.senha:
            print(f"{cor_verde}Você fez login com sucesso{restaurar_cor}")
        else:
            raise Exception(f"{cor_branca}{fundo_vermelho}Login ou senha inválidos{restaurar_cor}")
              
def menu_principal():
    print(f"\n{cor_azul}Por favor selecione uma opção a seguir:{restaurar_cor}\n")
    print(f"{cor_amarela}(1) {restaurar_cor}", end="")
    print("Logar como cliente.")
    print(f"{cor_amarela}(2) {restaurar_cor}", end="")
    print("Logar como Administrador.")
    print(f"{cor_amarela}(3) {restaurar_cor}", end="")
    print("Sair do programa.")
    while True:
        try:    
            escolha = int(input(f"{cor_amarela}\nR: {restaurar_cor}"))
            if escolha not in range(1,4):
                print(f"{cor_branca}{fundo_vermelho}Você precisar selecionar uma opção válida!{restaurar_cor}")
                continue
            break
        except:
            print(f"{cor_branca}{fundo_vermelho}Você precisar selecionar uma opção válida!{restaurar_cor}")
            pass
    return escolha
                         
def redirecionar1(escolha):
    if escolha == 1:
        print(f"{cor_verde}Você será direcionado para a tela de login, caro cliente!{restaurar_cor}")
        carregar()
        exit()
    elif escolha == 2:
        print(f"{cor_verde}Você será direcionado para a tela de login, Administrador!{restaurar_cor}")
        carregar()
        exit()
    elif escolha == 3:
        print(f"{cor_verde}Nos vêmos na próxima, então!\n{cor_amarela}Até mais!")
        exit()


#funcionamento do programa

df, dir_db = init_db()
escolha_do_menu_principal = menu_principal()
print(df)
redirecionar1(escolha_do_menu_principal)
root.mainloop()