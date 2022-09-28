class Coll():
    def __init__(self, d):
        self.ds = d
        self.cc = 0
    def __next__(self):
        if len(self.ds) <= self.cc:
            raise StopIteration
        self.cc+=1
        return self.ds[self.cc-1]

def main():
    co = Coll([1, 2, 3, 4, 5])
    while True:
        try:
            i = next(co)
            print(i, end=' ')
        except StopIteration:
            break

main()