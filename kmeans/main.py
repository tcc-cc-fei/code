file = open('respostas.csv', encoding='UTF-8', mode='r')
#abre arquivo para leitura

data = file.read()

# cada linha é uma pessoa, separada por \\n, as respostas dessa pessoa são separadas por \t
pessoa = data.strip()
pessoa = data.split('\n')

Mdados = []
norm1 = [
    6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 33, 35,
    36, 37, 48, 49, 50, 67, 72, 73, 74, 75, 76, 85, 86, 87, 88, 89, 90, 91, 95,
    103
]
norm2 = [
    9, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 38, 39, 40, 41, 42, 43, 44, 45,
    46, 47, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68,
    69, 70, 71, 77, 78, 79, 80, 81, 82, 83, 84, 92, 93, 94, 96, 97, 98, 99, 100
]
for id in pessoa:
  #separa as respostas de cada pessoa em uma lista e adiciona lista em uma matriz, de forma que, linha=pessoa, coluna=questão
  respostas = id.lower().replace(' do tempo', '').replace(",,",
                                                          ',-,').split(',')
  for item in respostas:
    i = respostas.index(item)
    #normalização, considerando quanto maior pior
    if i in norm1:
      item = item.replace("sim, algumas vezes", '4').replace(
          'sempre', "4").replace('frequentemente', "3").replace(
              'às vezes', "2").replace('raramente', "1").replace(
                  'nunca', "0").replace('na maior parte', "4").replace(
                      'em grande parte', "3").replace('um pouco', "2").replace(
                          'em uma pequena parte',
                          "1").replace('muito pouco', "0").replace(
                              'muito satisfeito',
                              "4").replace('nem/nem', '2').replace(
                                  'muito insatisfeito',
                                  "0").replace('insatisfeito', "1").replace(
                                      'satisfeito',
                                      "3").replace('não', "0").replace(
                                          "sim, diariamente",
                                          "4").replace("sim, semanalmente",
                                                       "3").replace(
                                                           "sim, mensalmente",
                                                           "2")
      respostas[i] = item
    if i in norm2:
      item = item.replace('sempre', "0").replace(
          'frequentemente',
          "1").replace('às vezes', "2").replace('raramente', "3").replace(
              'nunca', "4").replace('na maior parte', "0").replace(
                  'em grande parte', "1").replace('um pouco', "2").replace(
                      'em uma pequena parte',
                      "3").replace('muito pouco', "4").replace(
                          'eu não tenho colegas',
                          "0").replace('muito satisfeito', "0").replace(
                              'nem/nem',
                              '2').replace('muito insatisfeito', "4").replace(
                                  'insatisfeito',
                                  "3").replace('satisfeito', "1").replace(
                                      'eu não tenho um supervisor', '4')
      respostas[i] = item
  Mdados.append(respostas)

Dnorm = []

for linha in Mdados:
  holder = []
  mult = []
  holder.append(linha[0])  #id
  holder.append(linha[1])  #idade
  holder.append(linha[3])  #genero
  holder.append(linha[4])  #periodo
  holder.append(linha[5])  #ciclo
  holder.append(int(linha[6]) + int(linha[7]) + int(linha[8]) +
                int(linha[9]))  #demandas quantitativas
  holder.append(int(linha[10]) + int(linha[11]) +
                int(linha[12]))  #ritmos de tarefas
  holder.append(
      int(linha[13]) + int(linha[14]) + int(linha[15]) +
      int(linha[16]))  #demandas cognitivas
  holder.append(int(linha[17]) + int(linha[18]) +
                int(linha[19]))  #exigencias emocionais
  holder.append(
      int(linha[20]) + int(linha[21]) + int(linha[22]) +
      int(linha[23]))  #exigencia de esconder emocoes
  holder.append(
      int(linha[24]) + int(linha[25]) + int(linha[26]) + int(linha[27]) +
      int(linha[28]))  #influencia na faculdade
  holder.append(int(linha[29]) + int(linha[30]) +
                int(linha[31]))  #possibilidade de desenvolvimento
  holder.append(int(linha[32]) + int(linha[33]))  #variação de trabalhos
  holder.append(int(linha[34]) + int(linha[35]) +
                int(linha[37]))  #controle sobre tempo de trabalho
  holder.append(int(linha[38]) + int(linha[39]))  #Significado do curso
  holder.append(int(linha[40]) + int(linha[41]))  #Previbilisidade
  holder.append(int(linha[42]) + int(linha[43]) +
                int(linha[44]))  #Reconhecimento
  holder.append(int(linha[45]) + int(linha[46]) +
                int(linha[47]))  #clareza do curso
  holder.append(int(linha[48]) + int(linha[49]))  #conflitos de função
  holder.append(int(linha[50]))  #tarefas ilegitmas
  holder.append(
      int(linha[51]) + int(linha[52]) + int(linha[53]) +
      int(linha[54]))  #qualidade de liderança
  holder.append(int(linha[55]) + int(linha[56]) +
                int(linha[57]))  #apoio social dos professores
  holder.append(int(linha[58]) + int(linha[59]) +
                int(linha[60]))  #apoio social dos colegas
  holder.append(int(linha[61]) + int(linha[62]) +
                int(linha[63]))  #senso de comunidade no trabalho
  holder.append(
      int(linha[64]) + int(linha[65]) + int(linha[66]) + int(linha[67]) +
      int(linha[68]))  #compromisso com faculdade
  holder.append(int(linha[69]) + int(linha[70]) +
                int(linha[71]))  #engajamento na faculdade
  holder.append(int(linha[72]) + int(linha[73]))  #insegurança na faculdade
  holder.append(
      int(linha[74]) + int(linha[75]) + int(linha[76]) +
      int(linha[77]))  #insegurança na situação de estudo
  holder.append(int(linha[78]) + int(linha[79]))  #qualidade dos trabalhos
  holder.append(
      int(linha[80]) + int(linha[81]) + int(linha[82]) +
      int(linha[83]))  #satisfação na faculdade
  holder.append(
      int(linha[84]) + int(linha[85]) + int(linha[86]) + int(linha[87]) +
      int(linha[88]) + int(linha[89]))  #conflito de vida universitária
  holder.append(int(linha[90]) + int(linha[91]) +
                int(linha[92]))  #confiança horizontal
  holder.append(
      int(linha[93]) + int(linha[94]) + int(linha[95]) +
      int(linha[96]))  #confiança vertical
  holder.append(
      int(linha[97]) + int(linha[98]) + int(linha[99]) +
      int(linha[100]))  #justiça organizacional
  mult.append(linha[101])
  i = 102
    #Aqui deveria captar a 1ª resposta em forma de numero no mult.append da 137, então entrar no while para poder 
    # ler se foram colegas, professores, ambos ou nenhum ( dado por '-'), mas o 'não' das outras questões não está 
    # sendo substituído por número (feito no for da 21)
  while (linha[i] != '0' and linha[i] != '1' and linha[i] != '2'
         and linha != '3' and linha[i] != '4'):
    print(linha[i])
    mult.append(' ' + linha[i])
    i = i + 1
  holder.append(mult)  #fofocas e calunias
  mult = []
  mult.append(int(linha[i]))
  i += 1
  while (linha[i] not in '0 1 2 3 4'):
    mult.append(' ' + linha[i])
    i = i + 1
  holder.append(mult)  #conflitos e brigas
  mult = []
  mult.append(int(linha[i]))
  i += 1
  while (linha[i] not in '0 1 2 3 4'):
    mult.append(' ' + linha[i])
    i = i + 1
  holder.append(mult)  #provocação desagradavel
  mult = []
  mult.append(int(linha[i]))
  i += 1
  while (linha[i] not in '0 1 2 3 4'):
    mult.append(' ' + linha[i])
    i = i + 1
  holder.append(mult)  #ciberbullyng
  mult = []
  mult.append(int(linha[i]))
  i += 1
  while (linha[i] not in '0 1 2 3 4'):
    mult.append(' ' + linha[i])
    i = i + 1
  holder.append(mult)  #assédio
  mult = []
  Dnorm.append(holder)

from sklearn.cluster import KMeans
import numpy as np

kmeans = KMeans(n_clusters=2, random_state=0).fit(Dnorm)
#you can see the labels with:
print(kmeans.labels_)

# the output will be something like:
#array([0, 0, 0, 1, 1, 1], dtype=int32)
# the values (0,1) tell you to what cluster does every of your data points correspond to

#array([0, 1], dtype=int32)
#or see were the centres of your clusters are
kmeans.cluster_centers_

#home_data = pd.read_csv(Mdados, usecols = ['Id', 'Termo', 'median_house_value'])
#home_data.head()
#scikit-learn em conjunto o matplotlib
print(Dnorm)
file.close()
