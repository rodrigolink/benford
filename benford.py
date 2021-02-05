#codigo para testar lei de benford em dados eleitorais versao2
import os #para acessar a lista de arquivos na pasta
import csv #para processar os arquivos CSV

#ANO DA ELEICAO 2006, 2010, 2014 ou 2018
ano =2018
#TURNO DA ELEICAO 1 ou 2
turno = 1

if ano ==2018:
    #dado de entrada tem cabecalho?
    nao_cabecalho = False
    #posicao das colunas no dado de entrada - primeira coluna 0
    col_estado = 10
    col_cidade = 14
    col_zona = 15
    col_candidato = 19
    col_votos = 37
    col_turno = 5
else:
    #dado de entrada tem cabecalho?
    nao_cabecalho = True
    #posicao das colunas no dado de entrada - primeira coluna 0
    col_estado = 5
    col_cidade = 8
    col_zona = 9
    col_candidato = 11
    col_votos = 28
    col_turno = 3

#PROCESSANDO ARQUIVOS

#pasta onde estao os dados
path = 'dados/'
#lista com Sigla do Estado - Nome da cidade
cidades=set([])
#lista com Numero dos Candidatos
candidatos=set([])
#lista com estados
if ano ==2010:
    estados=['RR','AC','AP','DF','SE','RO','VT','TO','AL','MS','ES','MT','AM','RN','PB','PI','GO','SC','PA','MA','CE','PE','RJ','RS','ZZ','PR','BA','MG','SP']
else:
    estados=['RR','AC','AP','DF','SE','RO','TO','AL','MS','ES','MT','AM','RN','PB','PI','GO','SC','PA','MA','CE','PE','RJ','RS','ZZ','PR','BA','MG','SP']

#lista com regiao
regioes={
	'sul': ['RS','SC','PR'],
	'sudeste': ['SP','RJ','ES','MG'],
	'centro-oeste': ['MS','MT','GO','DF'],
	'norte': ['AC','AP','AM','PA','RO','RR','TO'],
	'nordeste': ['AL','BA','CE','MA','PB','PE','PI','RN','SE']
}

#para cada arquivo/cidade na pasta
for filename in os.listdir(path):
    if filename[-11:-7]==str(ano):
        print("Carregando dados de: %d" %ano)
        with open(path+filename) as csv_file:
#para cada cidade, adiciona na lista de cidade        
            csv_reader = csv.reader(csv_file, delimiter=';')
            print("Começando leitura do arquivo: "+filename)
#cria um dicionario com os dados da cidade
#estado, numero dos candidatos e numero de votos
            line_count = 0        
            for row in csv_reader:
                if (line_count>0 or nao_cabecalho) and (int(row[col_turno]) == turno):
                    cidade_nome = str(row[col_estado])+" - " + str(row[col_cidade])+" z-"+str(row[col_zona])
                    print(cidade_nome)
                    cidades.add(cidade_nome)
                    try:
                        vars()[str(row[col_estado])+ str(row[col_cidade])+str(row[col_zona])]
                    except KeyError:
                        vars()[str(row[col_estado])+ str(row[col_cidade])+str(row[col_zona])] = None
                    if vars()[str(row[col_estado])+ str(row[col_cidade])+str(row[col_zona])] is None:
                        vars()[str(row[col_estado])+ str(row[col_cidade])+str(row[col_zona])] = {}
                    
                    numero_votos_cidade = int(row[col_votos])
                    vars()[str(row[col_estado])+ str(row[col_cidade])+str(row[col_zona])][str(row[col_candidato])] =numero_votos_cidade
                    line_count += 1
                    candidatos.add(str(row[col_candidato]))
                else:
                    line_count+=1
                
            print(f'Processed {line_count} lines.')
            
        

#ao terminar todos os arquivos
print("Numeros de cidades processadas: %d" %len(cidades))

#MATEMÁGICA
from math import log10,sqrt 
    
#criando biblioteca para cada candidato
for candidato in candidatos:
    vars()["cand_"+str(candidato)]={}
    for numero in range(0,10):
        vars()["cand_"+str(candidato)][numero]=0
            
#criando biblioteca para cada candidato para cada estado
for candidato in candidatos:
    for estado in estados:
        vars()["cand_"+str(candidato)+"_"+str(estado)]={}
        for numero in range(0,10):
            vars()["cand_"+str(candidato)+"_"+str(estado)][numero]=0
			
#criando biblioteca para cada candidato para cada regiao
for candidato in candidatos:
    for regiao in regioes:
        vars()["cand_"+str(candidato)+"_"+str(regiao)]={}
        for numero in range(0,10):
            vars()["cand_"+str(candidato)+"_"+str(regiao)][numero]=0

#para cada zona, pegar o primeiro numero do numero de votos de cada candidato
for cidade in cidades:
    temp = cidade.replace(" - ", "")
    nome_cidade = temp.replace(" z-", "")
    for candidato in vars()[nome_cidade].keys():
        vars()["cand_"+str(candidato)][int(str(vars()[nome_cidade][candidato])[0])]+=1

#para cada estado, pegar o primeiro numero do numero de votos de cada candidato
for cidade in cidades:
    temp = cidade.replace(" - ", "")
    nome_cidade = temp.replace(" z-", "")
    for candidato in vars()[nome_cidade].keys():
        vars()["cand_"+str(candidato)+"_"+str(nome_cidade[0:2])][int(str(vars()[nome_cidade][candidato])[0])]+=1

#para cada regiao, pegar o primeiro numero do numero de votos de cada candidato
for regiao in regioes.keys():
    for candidato in candidatos:
        for estado in regioes[regiao]:
            for numero in range(0,10):
                vars()["cand_"+str(candidato)+"_"+str(regiao)][numero]+=vars()["cand_"+str(candidato)+"_"+str(estado)][numero]

#preparar plot
for candidato in candidatos:
    vars()["X_"+str(candidato)]=[]
    vars()["Y_"+str(candidato)]=[]
    total=0
    for numero in vars()["cand_"+str(candidato)].keys():
        if numero!=0:
            vars()["X_"+str(candidato)].append(int(numero))
            vars()["Y_"+str(candidato)].append(int(vars()["cand_"+str(candidato)][numero]))
            total+=int(vars()["cand_"+str(candidato)][numero])
    for i in range(0,9):
        if total!=0:
            vars()["Y_"+str(candidato)][i]/=float(total)

#preparar plot estados
for candidato in candidatos:
    for estado in estados:
        vars()["X_"+str(candidato)+str(estado)]=[]
        vars()["Y_"+str(candidato)+str(estado)]=[]
        total=0
        for numero in vars()["cand_"+str(candidato)+"_"+str(estado)].keys():
            if numero!=0:
                vars()["X_"+str(candidato)+str(estado)].append(int(numero))
                vars()["Y_"+str(candidato)+str(estado)].append(int(vars()["cand_"+str(candidato)+"_"+str(estado)][numero]))
                total+=int(vars()["cand_"+str(candidato)+"_"+str(estado)][numero])
        for i in range(0,9):
            if total!=0:
                vars()["Y_"+str(candidato)+str(estado)][i]/=float(total)

#preparar plot regioes
for candidato in candidatos:
    for regiao in regioes:
        vars()["X_"+str(candidato)+str(regiao)]=[]
        vars()["Y_"+str(candidato)+str(regiao)]=[]
        total=0
        for numero in vars()["cand_"+str(candidato)+"_"+str(regiao)].keys():
            if numero!=0:
                vars()["X_"+str(candidato)+str(regiao)].append(int(numero))
                vars()["Y_"+str(candidato)+str(regiao)].append(int(vars()["cand_"+str(candidato)+"_"+str(regiao)][numero]))
                total+=int(vars()["cand_"+str(candidato)+"_"+str(regiao)][numero])
        for i in range(0,9):
            if total!=0:
                vars()["Y_"+str(candidato)+str(regiao)][i]/=float(total)


#lei de benford
Ybenf=[]
for i in range(0,9):
    Ybenf.append(log10(1.+(1.0/float(i+1))))

#erro em relacao a lei de benford em todas as zonas
for candidato in candidatos:
    teste=0
    for i in range(0,9):
        teste+=(Ybenf[i]-vars()["Y_"+str(candidato)][i])**2
    vars()["sigma_"+str(candidato)]=sqrt(teste/float(9))

#erro em relacao a lei de benford por estado
for candidato in candidatos:
    for estado in estados:
        teste=0
        for i in range(0,9):
            teste+=(Ybenf[i]-vars()["Y_"+str(candidato)+str(estado)][i])**2
        vars()["sigma_"+str(candidato)+str(estado)]=sqrt(teste/float(9))
    
#erro em relacao a lei de benford por regiao
for candidato in candidatos:
    for regiao in regioes:
        teste=0
        for i in range(0,9):
            teste+=(Ybenf[i]-vars()["Y_"+str(candidato)+str(regiao)][i])**2
        vars()["sigma_"+str(candidato)+str(regiao)]=sqrt(teste/float(9))
	
#plotar graficos
import matplotlib.pyplot as plt

#grafico nacional por candidato
for candidato in candidatos:
    plt.scatter(vars()["X_"+str(candidato)], vars()["Y_"+str(candidato)], color = 'red')
    plt.plot(vars()["X_"+str(candidato)], Ybenf, color = 'blue')
    plt.title('Candidato N: %s' % candidato)
    plt.text(6,0.4,"sigma = %2.1f" % (100*vars()["sigma_"+str(candidato)]))
    plt.xlabel('Digito')
    plt.ylabel('Percentual de cada digito')
    plt.axis((0.5,9.5,-0.05,0.45))
    plt.savefig("imagens/graf_"+str(candidato)+".png")
    plt.show()

#graficos por estado por candidato
for candidato in candidatos:
    for estado in estados:
        plt.scatter(vars()["X_"+str(candidato)+str(estado)], vars()["Y_"+str(candidato)+str(estado)], color = 'red')
        plt.plot(vars()["X_"+str(candidato)+str(estado)], Ybenf, color = 'blue')
        plt.title('Candidato N: %s no estado: %s' % (candidato, estado))
        plt.text(6,0.4,"sigma = %.3f" % (100*vars()["sigma_"+str(candidato)+str(estado)]))
        plt.xlabel('Digito')
        plt.ylabel('Percentual de cada digito')
        plt.axis((0.5,9.5,-0.05,0.45))
        plt.savefig("imagens/graf_"+str(candidato)+"_"+str(estado)+".png")
        plt.show()

#grafico por regiao por candidato
for candidato in candidatos:
    for regiao in regioes:
        plt.scatter(vars()["X_"+str(candidato)+str(regiao)], vars()["Y_"+str(candidato)+str(regiao)], color = 'red')
        plt.plot(vars()["X_"+str(candidato)+str(regiao)], Ybenf, color = 'blue')
        plt.title('Candidato N: %s na regiao: %s' % (candidato, regiao))
        plt.text(6,0.4,"sigma = %.3f" % (100*vars()["sigma_"+str(candidato)+str(regiao)]))
        plt.xlabel('Digito')
        plt.ylabel('Percentual de cada digito')
        plt.axis((0.5,9.5,-0.05,0.45))
        plt.savefig("imagens/graf_"+str(candidato)+"_"+str(regiao)+".png")
        plt.show()


#grafico de candidato x estado
for candidato in sorted(candidatos):
    for estado in estados:
        if 100*vars()["sigma_"+str(candidato)+str(estado)]<3:
            cor = "blue"
        elif 100*vars()["sigma_"+str(candidato)+str(estado)]<6:
            cor = "green"
        elif 100*vars()["sigma_"+str(candidato)+str(estado)]<9:
            cor = "yellow"
        else:
            cor = "red"

        plt.scatter(estado,candidato,color=cor)
plt.tight_layout()
plt.title('Sigma calculado para todos os candidatos nos estados')
plt.xlabel('Estados')
plt.ylabel('Candidatos')
plt.savefig("imagens/sig_crossplot.png")
plt.show()

#grafico de candidato x regiao e Brasil
for candidato in sorted(candidatos):
    for regiao in regioes:
        if 100*vars()["sigma_"+str(candidato)+str(regiao)]<3:
            cor = "blue"
        elif 100*vars()["sigma_"+str(candidato)+str(regiao)]<6:
            cor = "green"
        elif 100*vars()["sigma_"+str(candidato)+str(regiao)]<9:
            cor = "yellow"
        else:
            cor = "red"
        plt.scatter(regiao,candidato,color=cor)
    if 100*vars()["sigma_"+str(candidato)]<3:
        cor = "blue"
    elif 100*vars()["sigma_"+str(candidato)]<6:
        cor = "green"
    elif 100*vars()["sigma_"+str(candidato)]<9:
        cor = "yellow"
    else:
        cor = "red"
    plt.scatter('BR',candidato,color=cor)
    
plt.tight_layout()
plt.title('Sigma calculado para todos os candidatos nas regiões e no Brasil')
plt.xlabel('Regiões e Brasil')
plt.ylabel('Candidatos')
plt.savefig("imagens/sig_crossplot_regioes.png")
plt.show()




print("Numeros de cidade processadas: %d" %len(cidades))
