class Validation():
    
    def __init__(self, word, mistake = 0, conditional = True) -> None:
        self.list_letters = []
        self.word = word
        self.mistake = mistake
        self.conditional = conditional 
                
    def check_validation(self, letter: str, masked_word: str) -> str:
                
        if len(letter) == 0:
            raise ValueError("Erro: Digite uma letra")
        
        elif len(letter) > 1:
            raise ValueError("Valor inválido, digite somente uma letra")
        
        elif not letter.isalpha():
            raise ValueError("A letra digitada não deve ser um número ou caractere especial")
        
        elif letter in self.list_letters:
            
            self.mistake += 1          
            if self.mistake == 6:
                print("Fim das chances, você perdeu :(\n")       
                self.check_repeat_play()     
                raise ValueError("")
            
            else:
                raise ValueError("Essa letra já foi usada")
        
        else:
            self.list_letters.append(letter)
            
            masked_word_list = list(masked_word)
    
            for index, char in enumerate(self.word):
                if char == letter:
                    masked_word_list[index] = letter
            
            new_masked_word = ''.join(masked_word_list)
            self.check_win(new_masked_word)
            return  new_masked_word   
        
    def check_win(self, masked_word: str):
        if '_' not in masked_word:
            print("Parabéns você venceu :)\n")
            self.check_repeat_play()
        
    def check_repeat_play(self):
        conditional = input("Digite 1 se quiser jogar denovo: ")
        if conditional != '1':
            self.conditional = False 
            print("\nObrigado pela jogatina. Te vejo em Breve :)")    