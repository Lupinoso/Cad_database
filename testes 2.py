import pandas as pd


dados = pd.DataFrame({'A': [1, 2, 3, 12],
                      'B': [4, 5, 6, 11],
                      'C': [7, 8, 9, 10]})


for dado in list(dados.loc[dados.shape[0]-1]):
    print(dado)


