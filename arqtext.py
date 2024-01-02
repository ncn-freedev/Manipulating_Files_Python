#Primeiro vamos abrir o arquivo
#Como o arquivo não está nessa pasta, devemos colocar o caminho de onde está
arquivo = open('./pasta_teste/texto.txt')
#vamos verificarse o arquivo está aberto com um print do arquivo.closed, se retornar false é pq o arquivo está aberto
print(f'Arquivo aberto: {arquivo.closed}\n')

'''Lendo o arquivo todo
print(f'Seu arquivo é:\n{arquivo.read()}\n')
'''

#Lendo linhas do arquivo
print(arquivo.readlines())#Retorna as linhas do arquivo guardadas em um vetor
#print(arquivo.readline()) #Lê as linhas do arquivo separadamente, dependendo de onde está o cursor


#Devemos fechar o aquivo após a utilização
arquivo.close()

#Verificando novamente, o resultado agora deve ser true
print(f'Arquivo aberto: {arquivo.closed}\n')