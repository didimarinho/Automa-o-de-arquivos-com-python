
from random import randint as rnd # random number generator


memReg = 'members.txt' # membros ativos
exReg = 'inactive.txt' # membros inativos
fee =('yes','no')

def genFiles(current,old): # função de gerenciamento de arquivos
    with open(current,'w+') as writefile: # criando arquivo com membros atuais
        writefile.write('Membership No  Date Joined  Active  \n') # cabeçalho do arquivo
        data = "{:^13}  {:<11}  {:<6}\n" # vai receber as datas randomicas pelo format

        for rowno in range(20): # para cada linha do arquivo
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25)) # gerando datas randomicas
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)])) # escrevendo as datas na linha 12 com format


    with open(old,'w+') as writefile: # criando arquivo com membros inativos
        writefile.write('Membership No  Date Joined  Active  \n') # cabeçalho do arquivo
        data = "{:^13}  {:<11}  {:<6}\n" # vai receber as datas randomicas pelo format
        for rowno in range(3): # para cada linha do arquivo
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25)) # gerando datas randomicas
            writefile.write(data.format(rnd(10000,99999),date,fee[1])) # escrevendo as datas na linha 21 com format


genFiles(memReg,exReg) # função recebendo arquivos






