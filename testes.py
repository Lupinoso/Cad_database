import openpyxl
import pandas as pd

caminho_arquivo_excel = 'data_base.xlsx'


nome_planilha = 'Administradores'  


arquivo_excel = openpyxl.load_workbook(caminho_arquivo_excel)


planilha = arquivo_excel[nome_planilha]


ultima_linha = planilha.max_row


nova_linha = ultima_linha + 1


dados = pd.DataFrame({'A': [1, 2, 3],
                      'B': [4, 5, 6],
                      'C': [7, 8, 9]})

print(pd.DataFrame.info(dados))

print(dados.loc[1])
print(dados.head())

for coluna, valor in enumerate(dados, start=1):
    planilha.cell(row=nova_linha, column=coluna, value=valor) 
    print("Valor:", valor)
    print("Coluna:", coluna)


arquivo_excel.save(caminho_arquivo_excel)


arquivo_excel.close()


