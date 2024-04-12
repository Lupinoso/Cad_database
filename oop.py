import pandas as pd
from sys import exit 
from time import sleep
import os
from tkinter import filedialog, Tk
from openpyxl import Workbook


#rodar loop do tk
if __name__ == "__main__":
    root = Tk() 
    root.withdraw()
#Senha mestre
senha_mestra = "abacaxi_assassino"

###parte visual###
cor_vermelha = '\033[31m'
cor_amarela = '\033[33m'
cor_branca = '\033[97m'
fundo_vermelho = '\033[41m'
cor_verde = '\033[32m'
restaurar_cor = '\033[0m'
cor_azul = '\033[34m'

def carregar():
    carregar_str = "Carregando"
    for letra in carregar_str:
        sleep(0.15)
        print(f"{cor_amarela}{letra}{restaurar_cor}",end="",flush=True)
    for x in range(4):
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
            except Exception:
                    print(f"{fundo_vermelho}{cor_branca}Por favor escolha um número!{restaurar_cor}")
                
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
            df_cliente = pd.read_excel(dir_padrao, sheet_name="Clientes")
            df_adm = pd.read_excel(dir_padrao, sheet_name="Administradores")
            return df_cliente, df_adm, dir_padrao
        else:
            print(f'{cor_vermelha}Banco de dados ainda nao foi criado!{restaurar_cor}')
            db_found, dir_db = load_db() 
            if db_found:
                df_cliente = pd.read_excel(dir_padrao, sheet_name="Clientes")
                df_adm = pd.read_excel(dir_padrao, sheet_name="Administradores")
                print(f"{cor_verde}Banco de dados carregado!{restaurar_cor}")
                return df_cliente, df_adm, dir_db
            elif not db_found:
                while True:
                    db_found, dir_db = load_db()
                    if db_found:
                        df_cliente = pd.read_excel(dir_padrao, sheet_name="Clientes")
                        df_adm = pd.read_excel(dir_padrao, sheet_name="Administradores")
                        print(f"{cor_verde}Banco de dados carregado!{restaurar_cor}")
                        return df_cliente,df_adm, dir_db
                    else:
                        pass

class Cliente():
    def __init__(self, nome, data_de_nascimento, email, cpf, senha):
        self.nome = nome
        self.data_nasc = data_de_nascimento
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
    print("Cadastrar Administrador.")
    print(f"{cor_amarela}(4) {restaurar_cor}", end="")
    print("Sair do programa.")
    while True:
        try:    
            escolha = int(input(f"{cor_amarela}\nR: {restaurar_cor}"))
            if escolha not in range(1,5):
                print(f"{cor_branca}{fundo_vermelho}Você precisar selecionar uma opção válida!{restaurar_cor}")
                continue
            break
        except:
            print(f"{cor_branca}{fundo_vermelho}Você precisar selecionar uma opção válida!{restaurar_cor}")
            pass
    if escolha == 1:
        if df_cliente.empty:
                print(f"{cor_vermelha}Não há clientes cadastrados!!\n", 
                      f"{cor_amarela}\bPor favor, entre como administrador para cadastrar um cliente!{restaurar_cor}")
                sleep(1)
                return False
        print(f"{cor_verde}Você será direcionado para a tela de login, caro cliente!{restaurar_cor}")
        carregar()
        return 1
    elif escolha == 2:
        if df_adm.empty:
            print(f"{cor_vermelha}Não há administradores cadastrados!!\n{restaurar_cor}")
            string = f"{cor_amarela}Redirecionando para o cadastro de administradores...{restaurar_cor}"
            for letra in string:
                print(f"{letra}", end="", flush=True)
                sleep(0.05)
            cad_adm = cadastrar_adm()
            if cad_adm == False:
                print(f"{cor_amarela}Retornando ao menu principal... {restaurar_cor}")
                sleep(1)
                return False
            elif cad_adm == True:
                return 2
        elif not df_adm.empty:
            usuario = str(input(f'{cor_azul}Por favor insira o nome do administrador que deseja logar!\n{cor_amarela}R: {restaurar_cor}'))
            print(usuario)
            return 2
        #falta fazer a parte se ja houver adms
        print(f"{cor_verde}Você será direcionado para a tela de login, Administrador!{restaurar_cor}")
        sleep(1)
        carregar()
        return 2
        
    elif escolha == 3:
        print(f"{cor_verde}Você será direcionado para a tela de cadastro de Administradores!{restaurar_cor}")
        carregar()
        return 3
    elif escolha == 4:
        print(f"{cor_verde}Nos vêmos na próxima, então!\n{cor_amarela}Até mais!")
        return 4

def cadastrar_adm():
    print(f'{cor_azul}Por favor selecione uma opção: {restaurar_cor}')
    sleep(1)
    print(f'''
    {cor_amarela}(1){restaurar_cor} Cadastrar administrador. {cor_vermelha}(NECESSÁRIO SENHA MESTRA){restaurar_cor}
    {cor_amarela}(2){restaurar_cor} Voltar ao menu anterior.
    ''')
    while True:
        try:
            escolha_cad_adm = int(input(f'{cor_azul}Escolha uma opção:\n{cor_amarela}R:{restaurar_cor} '))
            if escolha_cad_adm not in range(1,3):
                print(f"{cor_vermelha}Por favor selecione uma opção válida{restaurar_cor}")
                continue
            break
        except:
            print(f"{cor_vermelha}Por favor selecione uma opção válida{restaurar_cor}")
            pass
    if escolha_cad_adm == 1:
        r_senha_mestra = str(input(f'{cor_amarela}Por favor insira a senha mestra!\nR:{restaurar_cor} '))
        if r_senha_mestra == senha_mestra:
            print(f'{cor_verde}Senha Correta{restaurar_cor}')
            sleep(1)
            nome_adm = str(input('Qual o nome do administrador?\nR: '))
            cpf_adm = str(input('Qual o cpf do administrador?\nR: '))
            email_adm = str(input('Qual o email do administrador?\nR: '))
            senha_adm = str(input('Defina uma senha!\nR: '))
            data_nasc_adm = str(input('Qual o data de nascimento do administrador?\nR: '))
            adm_criado = Cliente(nome_adm, data_nasc_adm, email_adm, cpf_adm, senha_adm)
            carregar()
            df_adm.loc[df_adm.shape[0]+1] = [adm_criado.nome, adm_criado.data_nasc, adm_criado.email, adm_criado.cpf, adm_criado.senha]
            print(f'{cor_verde}Administrador criado com sucesso!{restaurar_cor}')
            sleep(1)
            return True
        elif r_senha_mestra != senha_mestra:
            print(f'{cor_vermelha}\nSenha incorreta{restaurar_cor}')
            sleep(1)
            return False
    elif escolha_cad_adm == 2:
        carregar()
        return False
            

#funcionamento do programa
if __name__ == "__main__":
    df_cliente, df_adm, dir_db = init_db()
    while True:
        escolha_do_menu_principal = menu_principal()
        if escolha_do_menu_principal == 1:
            print("vai logar como cliente")
            break
        elif escolha_do_menu_principal == 2: 
            break
        elif escolha_do_menu_principal == 3: 
            cadastrar_adm()
        elif escolha_do_menu_principal == 4:
            exit()
        elif not escolha_do_menu_principal:
            pass
        

root.mainloop()