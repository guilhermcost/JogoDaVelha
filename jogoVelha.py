# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 22:51:45 2021

@author: Guilherme Costa
"""

tabela = {0: -1, 1:1}

def posicoesVazias(estadoAtual):
    posicoes = []
    for i in range(len(estadoAtual)):
        for j in range(len(estadoAtual)):
            if estadoAtual[i][j] == -1:
                posicoes.append([i,j])
                
    return posicoes

def checaGanhador(estadoAtual):
# 1º checa formação em linha usando set
    for i in estadoAtual:
        if len(set(i)) == 1:
            vencedor = set(i).pop()
            if vencedor != -1:
                return tabela[vencedor]

#2º checa formação em coluna
    for i in range(0, len(estadoAtual)):
        coluna = []
        for j in estadoAtual:
            coluna.append(j[i])
        if len(set(coluna)) == 1:
            vencedor = set(coluna).pop()
            if vencedor != -1:
                return tabela[vencedor]
            
#3º checa formaçação em diagonal principal
    diagonal_p = []
    for i in range(0, len(estadoAtual)):    
        diagonal_p.append(estadoAtual[i][i])
    if len(set(diagonal_p)) == 1:
        vencedor = set(diagonal_p).pop()
        if vencedor != -1:
            return tabela[vencedor]

#4º checa formação em diagonal secundária
    diagonal_s = []
    dimensao = len(estadoAtual)
    for i in range(0, dimensao):    
        diagonal_s.append(estadoAtual[i][dimensao - 1 - i])
    if len(set(diagonal_s)) == 1:
        vencedor = set(diagonal_s).pop()
        if vencedor != -1:
            return tabela[vencedor]

#5º retorna 0 caso não tenha vencedor ainda        
    return 0

def minMax(tabuleiro, agente):
    ganhador = checaGanhador(tabuleiro)
    if ganhador != 0:
        return [ganhador, [-1,-1]]
    agente = agente % 2
    espacos_vazios = posicoesVazias(tabuleiro)
    if ganhador == 0 and len(espacos_vazios) == 0:
        return [0, [-1,-1]]
    melhor_valor = None
    proxMovimento = [-1,-1]
 
    for i in espacos_vazios:
        tabuleiro[i[0]][i[1]] = agente
        valor = minMax(tabuleiro, agente+1)[0]
        tabuleiro[i[0]][i[1]] = -1
        
        if(melhor_valor is None):
            melhor_valor = valor
            proxMovimento = i
        elif(agente == 1):
            if(valor > int(melhor_valor)):
                melhor_valor = valor
                proxMovimento = i
        elif(agente == 0):
            if(valor < int(melhor_valor)):
                melhor_valor = valor
                proxMovimento = i
        
    return [melhor_valor, proxMovimento]

#Recebimento de Entradas

dimensaoTabuleiro = int(input())
tabuleiro = []

for i in range (0, dimensaoTabuleiro):
    linha = input().rstrip().split(' ')
    linha = [int(val) for val in linha]
    tabuleiro.append(linha)
    
#fim das entradas

a = minMax(tabuleiro, 1)

string_saida = ''
string_saida += str(a[1][0])
string_saida += ','
string_saida += str(a[1][1])
print(string_saida)