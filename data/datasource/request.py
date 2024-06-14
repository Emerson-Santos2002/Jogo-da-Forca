import requests
from ..model.wordResponse import WordResponse

class RequestHTTP():
    
    URL: str = 'https://api.dicionario-aberto.net/random'
    
    def request_word(self) -> str:
        
        with requests.Session() as session: 
            
            try:
                
                response = session.get(self.URL, verify=True, timeout=10)
                response.raise_for_status()
                
                data_dict = response.json()
                
                if 'word' in data_dict:  
                    word_response = WordResponse(**data_dict)
                    return word_response.word    
                
                else:
                    raise ValueError('JSON inválido: não foi possível encontrar a chave "word"')
                               

            except requests.exceptions.HTTPError as http_erro:
                raise ValueError (f'ocorreu um erro HTTP: {http_erro}')
                
            except requests.exceptions.ConnectionError as conn_erro:
                raise ValueError (f'Ocorreu erro de conexão: {conn_erro}')
            
            except requests.exceptions.Timeout as timeout_erro:    
                raise ValueError (f'Tempo de requisição atingido: {timeout_erro}')
                
            except Exception as erro:
                raise ValueError (f'Ocorreu um erro: {erro}')