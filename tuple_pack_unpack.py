print("=======튜플=======")
a = 12,15
print(a)

b,c = a
print(f'b:{b}, c:{c}')

nums = 1,2,3,4,5 # == (1,2,3,4,5)

n1, n2, *others = nums      # 둘 이상의 값을 리스트로 묶을 때 *를 사용한다.
print(f'n1: {n1}, n2: {n2}, others: {others}')

first, *others, last = nums
print(f'first: {first}, others: {others}, last: {last}')

*others, n1, n2 = nums
print(f'others: {others}, n1: {n1}, n2: {n2}')

print("=======리스트=======")
nums = [1,2,3,4,5]
n1, n2, *others = nums
print(f'n1: {n1}, n2: {n2}, others: {others}')

print("=======함수 호출 및 반환에서 패킹, 언패킹=======")

def show_nums(n1, n2, *others):
    print(n1, n2, others, sep=',')
show_nums(1,2,3,4,5)

def sum(*nums):
    s = 0
    for i in nums:
        s += i
    return s

print(f'sum(1,2,3,4,5): {sum(1,2,3,4,5)}')

def show_man(name, age, height):
    print(name, age, height, sep=',')
p = ('Yoon', 22, 180)
show_man(*p)
lp = ['Yoon', 22, 180]
show_man(*lp)

p = 'Hong', (32, 178), '010-1234-56xx', 'Korea'
na, (ag, he), ph, ad = p
print(na, he)

na, (_,he), _, _ = p
print(na, he)

print("=======for 루프에서 패킹, 언패킹=======")
ps = [('Lee',172), ('Jung',182), ('Yoon',179)]
for n, h in ps:
    print(n, h, sep=',')
