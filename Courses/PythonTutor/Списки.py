#Четные индексы
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
n = input().split()
for i in range(0, len(n), 2):
    print(n[i])

#Четные элементы
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
a=input().split()
for i in a:
    if int(i)%2 == 0:
       print(i, end=' ')
       
#Больше предыдущего
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
a=input().split()
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

#Соседи одного знака
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
a = [int(i) for i in input().split()]
for i in range(1,len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break

#Наибольший элемент
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
a=[int(i) for i in input().split()]
z=max(a)
print(z)
print(a.index(z))

#Шеренга
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
a = [int(i) for i in input().split()]
x = int(input())
petya = 0
while petya < len(a) and a[petya] >= x:
    petya += 1
print(petya + 1)

#Количество различных элементов
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)
