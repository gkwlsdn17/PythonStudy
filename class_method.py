class Simple:
    num = 5
    @staticmethod
    def sm(i):
        print('st~ 5 + {0} = {1}'.format(i, Simple.num + i))
    @classmethod
    def cm(cls, i):
        print('cl~ 5 + {0} = {1}'.format(i, Simple.num + i))

def main():
    Simple.sm(3)
    Simple.cm(3)
    s = Simple
    s.sm(4)
    s.cm(4)

main()

