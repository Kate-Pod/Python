#Минимум из двух чисел
1: Даны два целых числа. Выведите значение наименьшего из них.
n=int(input())
m=int(input())
if m<n:
    print(m)
else:
    print(n)

    #Знак числа  
2:В математике функция sign(x) (знак числа) определена так:
sign(x) = 1, если x > 0,
sign(x) = -1, если x < 0,
sign(x) = 0, если x = 0.
Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.

x=int(input())
if x>0:
    print(1)
elif x<0:
    print(-1)
else:
    print(0)
 
#Шахматная доска
3:Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO. Программа получает на вход четыре числа от 1 до 8 
  каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

m1 = int(input())
n1 = int(input())
m2 = int(input())
n2 = int(input())
if (m1 + n1 + m2 + n2) % 2 == 0:
    print('YES')
else:
    print('NO')
 
#Високосный год 
4:Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что 
 в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
 
m=int(input())
if m%4==0 and m%100!=0 or m%400==0:
    print('YES')
else:
    print('NO')


    #Минимум из трех чисел
5: Даны три целых числа. Выведите значение наименьшего из них.
a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)

    #Сколько совпадает чисел
6:Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0
    (если все числа различны).
a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print('3')
elif a==b or a==c or b==c:
    print('2')
else:
    print('0')

    #Ход ладьи
7: Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом. 
  Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.
   m1 = int(input())
n1 = int(input())
m2 = int(input())
n2 = int(input())
if m1==m2 or n1==n2:
    print('YES')
else:
    print("NO") 
 
#Ход короля 
 8:   Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. Даны две различные клетки шахматной доски, определите, может ли король попасть с
  первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для
  второй клетки. Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую или NO в противном случае. 
        
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if ((x1 + 1 == y1) or (x1 - 1 == y1) or (x1 == y1)) and ( (x2 + 1 == y2) or (x2 - 1 == y2) or (x2 == y2)):
    print ('YES')
else:
    print ('NO')
 
#Ход слона
  9:  Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом.
    Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом.
    x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')

    #Ход ферзя
10:Шахматный ферзь ходит по диагонали, горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на
        вторую одним ходом.   
    x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
   
#Ход коня
  Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот. Даны две различные клетки шахматной доски, 
определите, может ли конь попасть с первой клетки на вторую одним ходом.  
    a=int(input())
b=int(input())
s=int(input())
d=int(input())
if (abs(a-s)==1 and abs(b-d)==2) or (abs(a-s)==2 and abs(b-d)==1) :
    print("YES")
else:
 print("NO")

    
    
    
    
