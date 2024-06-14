#Dia 5 - Jogo da Forca

import os
from data.model.word import Word
from data.datasource.request import RequestHTTP

def clear_screen():
    os.system('cls')
  
if __name__ == "__main__":
    
    CONDITIONAL = True
    clear_screen()
    print("Bem-Vindo ao Jogo da Forca")
    nickname = input("Digite seu nome de usuário: ")
    
    while CONDITIONAL:
         
        req = RequestHTTP()
        
        try:
            random_word = Word(req.request_word())
            print(random_word.word)
            print(nickname)
                     
        except ValueError as e:
            print(f'Erro: {e}')   