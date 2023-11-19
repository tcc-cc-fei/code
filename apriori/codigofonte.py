from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import matplotlib.pyplot as plt
from unidecode import unidecode
import pandas as pd
import re

def plotarGraficos(dataframe,arg1,arg2,titulo):
    dataframe.plot(x=arg1, y=arg2, kind='line', legend=False)
    plt.title(titulo)
    plt.xlabel(arg1)
    plt.ylabel(arg2)
    plt.xticks(fontsize=8) 
    plt.yticks(fontsize=8) 
    plt.show()

def remover_caracteres_especiais(txt):
    txt= re.sub(r'[\xa0\n]', '', txt)
    return txt

def remover_acentos(palavra):
    if isinstance(palavra, str):
        return unidecode(palavra).replace("deg","º")
    elif isinstance(palavra, int):
        return palavra
    
def dropColunas(df, coluna):
    df = df.drop(coluna, axis=1)
    return df

def LerArquivo():    
    df = pd.read_excel('questionario.xlsx')
    df.drop(df.columns[[1,2,3,4,5,6]], axis=1, inplace=True)
    df=df.drop_duplicates()
    return df

def Transformar_Em_Dummies(df,coluna,prefixo,tipo):
    for item in range(len(coluna)):
        dummies = pd.get_dummies(df[coluna[item]], prefix=prefixo[item],dtype=tipo[item])
        print(dummies)
        df = pd.concat([df, dummies], axis=1)
        df = dropColunas(df, coluna[item])
    return df

def DiscretizarNotas(df,coluna_atual,nova_coluna,bins,labels):
    novo_df=pd.DataFrame()
    novo_df[nova_coluna] = pd.cut(df[coluna_atual], bins=bins, labels=labels)
    df[coluna_atual]=(novo_df[nova_coluna])
    return df

def Renumerar_Questoes(df):
    controle=1
    for i in range(7,149,1):
        novo_nome=f"Questao_{str(i)}"
        df.rename(columns = {df.columns[controle]:novo_nome}, inplace = True)
        controle=controle+1
    return df

def Padronizacao(df,escala,op_resp):
    for chave,valor in escala.items():
        print(chave,valor)
        for item in valor:
            if chave=='q_positiva':
                lista=op_resp.get("resp_positiva")
                coluna=f"Questao_{item}"
                df[coluna] = df[coluna].astype("str")  
                resultado_positivo = df.query(f'{coluna}=={lista}')
                indices_positivos=(list(resultado_positivo[coluna].index))
                indices_negativos = df.loc[~df.index.isin(indices_positivos)]
                indices_negativos=list(indices_negativos[coluna].index)
                df.loc[indices_positivos, coluna] = 1
                df.loc[indices_negativos, coluna] = 0
            else:
                lista=op_resp.get("resp_negativa") 
                coluna=f"Questao_{item}"
                df[coluna] = df[coluna].astype("str")  
                resultado_negativo = df.query(f'{coluna}=={lista}')
                indices_negativos=(list(resultado_negativo[coluna].index))
                indices_positivos = df.loc[~df.index.isin(indices_negativos)]
                indices_positivos=list(indices_positivos[coluna].index)
                df.loc[indices_positivos, coluna] = 0
                df.loc[indices_negativos, coluna] = 1

    return df    



def Definicao_Padroes(df):
    escala_10={"q_positiva":[143,145,146,147,148],"q_negativa":[144]}
    escala_5_m={"q_negativa":[103,106,108,110,112,114,116]}
    escala_1={"q_positiva":[16,25,26,27,28,29,33,35,36,37],"q_negativa":[7,8,9,11,14,15,17,18,19,21,24,86]}
    escala_2={"q_positiva":[30,31,32,39,40,41,42,43,44,45,46,47,48,65,66,67,69,79,80,93,94,95,97,98,99,100,101],"q_negativa":[12,13,20,22,23,49,50,51,73,74,75,76,77,87,88,89,90]}
    escala_1_r={"q_positiva":[10],"q_negativa":[34,38,68]}
    escala_2_r={"q_positiva":[78],"q_negativa":[91,92,96]}
    escala_6={"q_positiva":[81,82,83,84,85]}
    escala_4={"q_negativa":[102,104,105,107,109,111,113,115]}
    escala_7={"q_positiva":[118]}
    escala_numeral={"q_positiva":[119]}
    escala_9={"q_negativa":[120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142]}
    escala_3={"q_positiva":[70,71,72]}
    escala_1_plus={"q_positiva":[56,57,58]}
    escala_1_plus_plus={"q_positiva":[59,60,61,62,63,64],"q_negativa":[117]}
    escala_2_plus={"q_positiva":[52,53,54,55]}
    escala_10_resps={"resp_positiva":['Encaixa um pouquinho','Nao encaixa'],"resp_negativa":['Encaixa perfeitamente','Encaixa muito bem']}
    escala_5_m_resps={"resp_negativa":['Colegas;','Professores;','Colegas;Professores;']}
    escala_1_resps={"resp_positiva":['Raramente','Nunca'],"resp_negativa":['Sempre','Frequentemente']}
    escala_2_resps={"resp_positiva":['Em uma pequena parte','Muito Pouco'],"resp_negativa":['Na maior parte','Em grande parte']}
    escala_1_r_resps={"resp_positiva":['Nunca','Raramente'],"resp_negativa":['Frequentemente','Sempre']}
    escala_2_r_resps={"resp_positiva":['Em uma pequena parte','Muito Pouco'],"resp_negativa":['Em grande parte','Na maior parte']}
    escala_6_resps={"resp_positiva":['Insatisfeito','Muito Insatisfeito']}
    escala_4_resps={"resp_negativa":['Sim, diariamente','Sim, semalmente','Sim, mensalmente','Sim, algumas vezes']}
    escala_7_resps={"resp_positiva":['Regular','Ruim']}
    escala_numeral_resps={"resp_positiva":['0-2','3-5']}
    escala_9_resps={"resp_negativa":['Sempre','Grande parte do tempo']}
    escala_3_resps={"resp_positiva":['Nunca','Raramente']}
    escala_1_plus_resps={"resp_positiva":['Raramente','Nunca','Eu nao tenho supervisor']}
    escala_1_plus_resps={"resp_positiva":['Raramente','Nunca','Eu nao tenho colegas'],"resp_negativa":['Sempre','Frequentemente']}
    escala_2_plus_resps={"resp_positiva":['Em uma pequena parte','Muito Pouco','Eu nao tenho supervisor']}
    df=Padronizacao(df,escala_10,escala_10_resps)
    df=Padronizacao(df,escala_5_m,escala_5_m_resps)
    df=Padronizacao(df,escala_1,escala_1_resps)
    df=Padronizacao(df,escala_2,escala_2_resps)
    df=Padronizacao(df,escala_1_r,escala_1_r_resps)
    df=Padronizacao(df,escala_2_r,escala_2_r_resps)
    df=Padronizacao(df,escala_6,escala_6_resps)
    df=Padronizacao(df,escala_4,escala_4_resps)
    df=Padronizacao(df,escala_7,escala_7_resps)
    df=Padronizacao(df,escala_numeral,escala_numeral_resps)
    df=Padronizacao(df,escala_9,escala_9_resps)
    df=Padronizacao(df,escala_3,escala_3_resps)
    df=Padronizacao(df,escala_1_plus,escala_1_plus_resps)
    df=Padronizacao(df,escala_1_plus_plus,escala_1_plus_resps)
    df=Padronizacao(df,escala_2_plus,escala_2_plus_resps)
    return df
df=LerArquivo()

df.columns = [remover_caracteres_especiais(coluna) for coluna in df.columns]
df = df.map(remover_acentos)


colunas_dummies=['Qual a sua idade?','Com qual gênero você se identifica?','Em qual periodo você estuda?','Qual ciclo você está atualmente?','Você deseja mudar de turno?']
prefixo_colunas=['Idade','Genero','Periodo',None,'Turno']
dtype_coluna=[int,int,int,int,int]
df=Transformar_Em_Dummies(df,colunas_dummies,prefixo_colunas,dtype_coluna)
bins = [0,2,5,6,9,10]
labels = ['0-2', '3-5', '6', '7-9','10']
df=DiscretizarNotas(df,'Se você avaliar o melhor estado de saúde concebível em 10 pontos e o pior em 0 pontos.Quantos pontos você daria ao seu estado de saúde atual?','SaudeMental',bins,labels)
df=Renumerar_Questoes(df)
df=Definicao_Padroes(df)
df=dropColunas(df,'ID')

itens_spt_min = apriori(df, min_support=0.7, use_colnames=True)



"""itens_spt_min.plot(x='itemsets', y='support', kind='line', legend=False)
plt.title('Suporte por item')
plt.xlabel('Item')
plt.ylabel('support')
plt.xticks(fontsize=5) 
plt.yticks(fontsize=5) 
plt.show()"""

rules = association_rules(itens_spt_min, metric= "confidence", min_threshold = 0)
rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False]) 
rules = rules.drop('zhangs_metric', axis=1)
rules = rules.drop('leverage', axis=1)
rules = rules.drop('conviction', axis=1)
rules = association_rules(itens_spt_min, metric= "confidence", min_threshold = 0.8)
rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False]) 

"""plotarGraficos(rules,'confidence','lift','Lift por confiança')
plotarGraficos(rules,'antecedents','lift','Lift por antecedente')
plotarGraficos(rules,'consequents','lift','Lift por consequente')
plotarGraficos(rules,'antecedents','confidence','Confiança por antecedente')
plotarGraficos(rules,'consequents','confidence','Confiança por consequente')"""

lift_maior_1 = rules[rules['lift'] > 1]
lif_menor_1=rules[rules['lift'] < 1]
lift_igual_1=rules[rules['lift']==1]

plotarGraficos(lift_maior_1,'confidence','lift','Lift por confiança - Filtrando lift maior que 1')
plotarGraficos(lift_maior_1,'antecedents','lift','Lift por antecedente - Filtrando lift maior que 1')
plotarGraficos(lift_maior_1,'consequents','lift','Lift por consequente - Filtrando lift maior que 1')
plotarGraficos(lift_maior_1,'antecedents','confidence','Confiança por antecedente - Filtrando lift maior que 1')
plotarGraficos(lift_maior_1,'consequents','confidence','Confiança por consequente - Filtrando lift maior que 1')

plotarGraficos(lif_menor_1,'confidence','lift','Lift por confiança - Filtrando lift menor que 1')
plotarGraficos(lif_menor_1,'antecedents','lift','Lift por antecedente - Filtrando lift menor que 1')
plotarGraficos(lif_menor_1,'consequents','lift','Lift por consequente - Filtrando lift menor que 1')
plotarGraficos(lif_menor_1,'antecedents','confidence','Confiança por antecedente - Filtrando lift menor que 1')
plotarGraficos(lif_menor_1,'consequents','confidence','Confiança por consequente - Filtrando lift menor que 1')


