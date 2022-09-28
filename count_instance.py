class Simple:
    count = 0
    def __init__(self):
        Simple.count += 1
    # def get_count(self):
    #     return Simple.count

    @staticmethod
    def get_count():
        return Simple.count

def main():
    # s1 = Simple()
    # print(s1.get_count())
    # s2 = Simple()
    # print(s1.get_count())
    # s3 = Simple()
    # print(s1.get_count())

    print(Simple.get_count())
    s = Simple()
    print(Simple.get_count())

main()