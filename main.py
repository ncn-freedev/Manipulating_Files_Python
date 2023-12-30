import os


# Criando um diretório
if os.path.exists('python') is False:
    os.mkdir('python')
else:
    print('Diretório já existe')

# Verificando se existe o diretório
print(os.path.exists('python'))
print(os.path.exists('flutter'))

# Criando arquivos
if os.path.exists('flutter.py') is False:
    os.mknod('flutter.py')
else:
    print('Arquivo já existe')

#Verificando novamente
print(os.path.exists('flutter.py'))

"""Renomeando um arquivo. 
O método só funciona para arquivos que estejam no diretório atual
Para renomear arquivos ou diretórios fora da pasta atual, deve se utilizar o caminho relativo ou absoluto
do arquivo que será alterado e citar o novo caminho do arquivo ou diretório que será nomeado
O método pode ser usado tbm para alterar a extensão do arquivo
O método também funciona para renomear diretórios
"""
#os.rename('flutter.py', 'FLUTTER.py')

#Removendo um arquivo
#os.remove("FLUTTER.py")
os.remove('flutter.py')
if os.path.exists('FLUTTER.py') is False:
    print('Arquivo removido')
else:
    print('Arquivo ainda existe')

"""O os.remove só serve para apagar arquivos, para apagar diretórios
deve ser usado o método abaixo"""
os.rmdir('python')
if os.path.exists('python') is False:
    print('Diretório removido')
else:
    print('Diretório ainda existe')

