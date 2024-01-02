'''Vamos agora ver a forma pythoniana de ler e escrever arquivos'''

#Para abrir o arquivo
#Dessa forma, o arquivo é aberto, utilizado e fechado automaticamente logo após
with open('./pasta_teste/texto.txt') as arquivo:
    print(arquivo.read())
    #vamos verificar se o arquivo está aberto com um print do arquivo.closed, se retornar false é pq o arquivo está aberto
    print(f'Arquivo aberto: {arquivo.closed}\n')
#Verificando novamente, o resultado agora deve ser true
print(f'Arquivo aberto: {arquivo.closed}\n')