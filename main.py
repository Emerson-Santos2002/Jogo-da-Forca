#Dia 5 - Jogo da Forca

import os
from util.validation import Validation
from data.datasource.request import RequestHTTP

def clear_screen():
    os.system('cls')        
                           
if __name__ == "__main__":
    
    clear_screen()
    print("Bem-Vindo ao Jogo da Forca")
    nickname = input("Digite seu nome de usuário: ")
    clear_screen()
    
    print(f"Boa sorte {nickname}\n")
    print("1-Digite apenas uma letra por vez")
    print("2-Adivinhação de uma letra por rodada")
    print("3-Vence ao adivinhar todas as letras")
    print("4-Perde ao errar 6 letras")
    input("Pressione Enter para continuar")
    clear_screen()
      
    try:
        req = RequestHTTP()
        random_word = str(req.request_word())
        
        validation = Validation(random_word)
        masked_word = ""

        for i in enumerate(random_word):
            masked_word += '_'
        
        while validation.conditional:
            
            try:
                print(random_word)
                print(f"'{masked_word}'\n")
                letter = input(f"Digite uma letra {nickname}: ")
                clear_screen()
    
                masked_word = validation.check_validation(letter=letter, masked_word=masked_word)
            
            except ValueError as erro:
                print(f"{erro}\n")    
              
    except ValueError as e:
        print(f"Erro: {e}")