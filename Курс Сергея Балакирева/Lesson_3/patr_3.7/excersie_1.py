import sys

class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)
        
    def __bool__(self):
        return self.score > 0
    
# считывание списка из входного потока (эту строчку и список lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

players = [Player(*i.split('; ')) for i in lst_in]
players_filtered = list(filter(lambda x: bool(x), players))
