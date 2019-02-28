# -*- coding: utf-8 -*-
"""Exemplo_SOM

Interpretador de Assuntos em Mensagens

"""
'''
import nltk  # Natural Language Toolkit
nltk.download('rslp')  #raiz das palavras
nltk.download('punkt')  #trabalhar com pontuação

# tokenize pega uma string e coloca em um vetor
palavra = nltk.tokenize.word_tokenize('dúvida    carro casa')
print (palavra)
stemmer = nltk.stem.RSLPStemmer()   #pegar o radical da palavra
palavra2 = stemmer.stem('dúvida')
print (palavra2)

import unicodedata
palavra_sem_acento = unicodedata.normalize('NFKD','dúvida').encode('ASCII','ignore').decode('utf-8')
print(palavra_sem_acento)
'''


def transforma_msgs_binario(msgs, palavras_chaves):
    'Transforma a matriz de  msgs em uma de vetor de binários'
    X = []
    for msg in msgs:
        data = []
        aux = False    #verificar se não encontrou nenhuma palavra chave
        # Transformação em vetor
        for palavra in palavras_chaves:
            if(palavra.lower() in msg.lower()):
                aux = True
                data.append(1)
            else:
                data.append(0)
        if aux == True:
            # Transformar em matriz
            X.append(data)
    return X
def calcula_w(som, matriz):
    'Retorna um vetor de w calculados pela SOM'
    w_matriz = []
    for vetor in matriz:
        w = som.winner(vetor)
        w_matriz.append(w)
    return w_matriz
    
def transformador_palavra_binario(palavras_chaves):
    'Retorna uma matriz com as  palavras chaves com 0 e 1'
    matriz = []
    for matriz_posicao in range(0,len(palavras_chaves)):
        vetor = []
        for vetor_posicao in range(0,len(palavras_chaves)):
            if (matriz_posicao == vetor_posicao):
                vetor.append(1)
            else:
                vetor.append(0)
        matriz.append(vetor)
    return matriz


def exibe_grafico(w, palavra, tamanho, cor):
    'Exibe a palavra no gráfico'
    plt.text(w[0], w[1], palavra, size=tamanho,color = cor, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
         

# Ler lista de emails
msg1 = "Professor, não estou conseguindo eNtender o banco de dados da som"
msg2 = "Professor, eu tenho uma sUgestão para um exercício de regressao linear"
msg3 = "Eu não Entendi o exemplo do K-means da eleição"
msg4 = "Não entendi bem aquele assunto da aula de ontem"
msg5 = "Tenho uma sugestão para melhorar o entendimento do exercício de perceptron"
msg6 = "TENHO DÚVIDA QUANTO AOS EXERCICIOS QUE DEVEMOS ELABORAR PARA A AULA DE AMANHÃ."
msg7 = "AMIGOS, AGUARDO CONTATO NO DISCORDIA CASO POSSAM SUGERIR ALGUNS EXEMPLOS SOBRE K-MEANS ."
msg8 = "ENTENDO QUE OS ALGORÍTIMOS APRESENTADOS EM SALA JÁ NOS CAPACITAM A PERCEBER OS BENEFÍCIOS DA AUTOMACAO DE ROTINAS DE INTERPRETAÇÃO DE DADOS EMPREGANDO MACHINE LEARN."
msg9 = "ESTOU ENVIANDO ALGUNS EXERCICIOS PARA COMPARAR OS ALGORITIMOS SOM, K-MEANS E MLP."
msg10 = "OS INTEGRANTES DA NOSSA TURMA PODERÃO APRENDER COMO APLICAR MODELOS OTIMIZADOS?"
msg11 = "A REGRESSÃO LINEAR E MMQ SAO ELEMENTOS EMBUTIDOS NOS ALGORITIMOS DE MACHINE LEARNING?"
msg12 = "COMO PODEMOS APLICAR O PERCEPTRON?"
msg13 = "QUAIS MODELOS DE OTIMIZAÇAO PODEMOS APLICAR EM SALA?"
msg14 = "OS TESTES DE PARADA PODEM SER APLICADOS PARA MLP E REDES NEURAIS ?"
msg15 = "COMO DEVEMOS DEFINIR O TAMANHO INICIAL DA MATRIZ DE NEURONIO?"
msg16 = "QUAIS CAMADAS ESTÃO PRESENTES NAS REDES NEURAIS"
msg17 = "NAS REDES NEURAIS, COM É FEITO O REPROCESSAMENTO DOS FATORES QUE PONDERAM CADA PESO? "


msg_test1 = "Ola professor, gostaria te tirar uma duvida sobre o banco de dados da rede som"
msg_test2 = "Professor, não entendi direito como funciona o modelo do K-means"
msg_test3 = "Gostaria de sugerir um exemplo de aplicação de rede neurais"
msg_test4 = "Gostaria de aplicar o Perceptron em um exercício que achei na internet, mas estou com duvida na hora de fazer o código"
msg_test5 = "Professor, gostaria de fazer mais exercícios sobre a MLP"

msg_valida = [msg_test1, msg_test2, msg_test3, msg_test4, msg_test5]


msgs = [msg1, msg2, msg3, msg4, msg5, msg6, msg7,msg8, msg9, msg10, msg11, msg12, msg13, msg14, msg15, msg16, msg17]
# Definir palavra chave

palavras_chaves = ["duv", "sug", "entend","exerci","model","nota","avalia",
                   "exempl","assunt","Machine","Learning", "aprend","revis", "means",
                   "regres", "som","neura", "perceptron", "MLP", "otimiz"]

#Transforma o vetor de msgs em uma matriz de binarios
X_treino = transforma_msgs_binario(msgs, palavras_chaves)
X_valida = transforma_msgs_binario(msg_valida, palavras_chaves)


# Jogar no SOM

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X_treino = sc.fit_transform(X_treino)

# Training the SOM
Tamanho_eixo_X = 25
Tamanho_eixo_Y = 25
from minisom import MiniSom
som = MiniSom(x = Tamanho_eixo_X, y = Tamanho_eixo_Y, input_len = len(palavras_chaves), sigma = 1.0, learning_rate = 0.5, random_seed=3)
som.random_weights_init(X_treino)
som.train_random(data = X_treino, num_iteration = 80)


# Visualizing the results



matriz_palavras_chaves = transformador_palavra_binario(palavras_chaves)
# Calculo de cada w
w_treino = calcula_w(som, matriz_palavras_chaves)
w_valida = calcula_w(som, X_valida)
print(w_treino)

import matplotlib.pyplot as plt

plt.axis([0,Tamanho_eixo_X,0,Tamanho_eixo_Y])

#Palavras bases
for w_posicao in range(0, len(palavras_chaves)):
    exibe_grafico(w_treino[w_posicao], palavras_chaves[w_posicao], 10, 'b')
   
# Validacao
for w_posicao in range(0, len(msg_valida)):
    exibe_grafico(w_valida[w_posicao], "T" + str(w_posicao+1), 9, 'r')
 
    
''' 
Cores:   
‘b’ 	blue
‘g’ 	green
‘r’ 	red
‘c’ 	cyan
‘m’ 	magenta
‘y’ 	yellow
‘k’ 	black
‘w’ 	white
'''