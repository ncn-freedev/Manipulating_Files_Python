import os


# Criando um diretório
os.mkdir('python')

# Verificando se existe o diretório
print(os.path.exists('python'))
print(os.path.exists('flutter'))

# Criando arquivos
os.mknod('flutter.py')

#Verificando novamente
print(os.path.exists('flutter.py'))
