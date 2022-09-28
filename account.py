class Account:
    def __init__(self, aid, abl):
        self.aid = aid
        self.abl = abl
    def __iadd__(self, m):
        self.abl += m
        return self
    def __isub__(self, m):
        self.abl -= m
        return self
    def __str__(self):
        return '{0}, {1}'.format(self.aid, self.abl)

def main():
    acnt = Account('James01', 100)
    acnt += 130
    print(acnt)
    acnt -= 50
    print(acnt)

main()