'''Vamos agora ver a forma pythoniana de ler e escrever arquivos'''

def ler_arquivo():
    #Para abrir o arquivo
    #Dessa forma, o arquivo é aberto, utilizado e fechado automaticamente logo após
    #A função open tem um parâmetro padrão de leitura, que seria o 'r' depois do nome do arquivo a ser aberto
    #O parâmetro 'r' significa read, leitura. Para escrita utilizamos o parâmetro 'w', escrita
    with open('./pasta_teste/texto.txt') as arquivo:
        print(arquivo.read())
        #vamos verificar se o arquivo está aberto com um print do arquivo.closed, se retornar false é pq o arquivo está aberto
        print(f'Arquivo aberto: {arquivo.closed}\n')
    #Verificando novamente, o resultado agora deve ser true
    print(f'Arquivo aberto: {arquivo.closed}\n')

def escrever_arquivo():
    #Escrevendo um novo dado no arquivo
    #Utilizando o parâmetro 'w' para indicar escrita no arquivo
    #Utilizando da forma posta aqui, o que for escrito pela função irá sobreescrever o que está no arquivo
    with open('./pasta_teste/texto.txt', 'w') as arquivo:
        arquivo.write('Esse texto foi inserido por uma função write no arquivo!')
        #vamos verificar se o arquivo está aberto com um print do arquivo.closed, se retornar false é pq o arquivo está aberto
        print(f'Arquivo aberto: {arquivo.closed}\n')
    #Verificando novamente, o resultado agora deve ser true
    print(f'Arquivo aberto: {arquivo.closed}\n')

def escrever_no_final(novo_dado):
    #Escrevendo um novo dado no arquivo
    #Utilizando o parâmetro 'a' para indicar escrita onde o cursos parou no arquivo
    #O 'a' significa append e essa função irá adicionar, sem sobrescrever, a informação passada no arquivo, 
    #começando da posição atual do currsor, por isso é importante colocar o cursos no final do arquivo para dar continuidade
    with open('./pasta_teste/texto.txt', 'a') as arquivo:
        arquivo.write(novo_dado)
        #vamos verificar se o arquivo está aberto com um print do arquivo.closed, se retornar false é pq o arquivo está aberto
        print(f'Arquivo aberto: {arquivo.closed}\n')
    #Verificando novamente, o resultado agora deve ser true
    print(f'Arquivo aberto: {arquivo.closed}\n')

if __name__ == '__main__':
    ler_arquivo()
    escrever_no_final('\nEsse é o novo dado escrito no arquivo\n')
    ler_arquivo()