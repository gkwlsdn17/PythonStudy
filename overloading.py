class Account:
    def __init__(self, aid, abl):
        self.aid = aid
        self.abl = abl
    def __add__(self, m):
        self.abl += m
        print('__add__')
    def __sub__(self, m):
        self.abl -= m
        print('__sub__')
    def __call__(self):
        print('__call__')
        return str(self.aid) + ':' + str(self.abl)

def main():
    acnt = Account('James01', 100)
    acnt + 100
    acnt - 50
    print(acnt())

main()