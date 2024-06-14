class WordResponse():
    
    def __init__(self, wid: int, sense: int, word: str) -> None:
        self.wid = wid
        self.sense = sense
        self.word = word