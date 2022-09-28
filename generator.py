import sys


def gen_num():
    # yield가 하나라도 들어가면 제너레이터
    print('first number')
    yield 1 # 첫 번째 next 호출에서 이 문장까지 실행됨
    print('second number')
    yield 2 # 두 번째 next 호출에서 이 문장까지 실행됨
    print('third number')
    yield 3 # 세 번째 next 호출에서 이 문장까지 실행됨


gen = gen_num()

print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # ERROR: StopIteration

def pows(s):
    r = []
    for n in s:
        r.append(n**2)
    return r

def gpows(s):
    for n in s:
        yield n ** 2

st = pows([1,2,3,4,5,6,7,8,9])
for i in st:
    print(i, end = ' ')
print(f'\nsys.getsizeof(st): {sys.getsizeof(st)}')

st = gpows([1,2,3,4,5,6,7,8,9])
for i in st:
    print(i, end = ' ')
print(f'\nsys.getsizeof(st): {sys.getsizeof(st)}')

def get_nums():
    ns = [0,1,0,1,0,1]
    yield from ns

nums = get_nums()
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))