from random import shuffle
from secrets import choice
import string

def gerador_senhas():
    len = (int(input('Diga o número de dígitos que deseja na senha:')))
    lista_ascii = [i for i in string.printable]
    del lista_ascii[94:]
    password = []
    for i in range(len):
        password.append(choice(lista_ascii))
        shuffle(password)
    print('\nSua senha segura:\n\n'+ ''.join(password) + '\n')
    
if __name__=='__main__':
    gerador_senhas()