#Делаем срезы
Дана строка.
Сначала выведите третий символ этой строки.
Во второй строке выведите предпоследний символ этой строки.
В третьей строке выведите первые пять символов этой строки.
В четвертой строке выведите всю строку, кроме последних двух символов.
В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
В седьмой строке выведите все символы в обратном порядке.
В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
В девятой строке выведите длину данной строки.
n=input()
print(n[2])
print(n[-2]) #предпоследний символ
print(n[:5]) #5 символов
print(n[0:-2]) #4 строка
print(n[0::2]) #все четные
print(n[1::2]) #все нечетные
print(n[::-1]) #в обратном порядке
print(n[::-2])
print(len(n))

#Количество слов
Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения задачи метод count.
n=input()
print(n.count(' ')+1)

#Две половинки
Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, то длина первой части должна быть на один символ больше). Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.
s = input()
l = len(s)//2+len(s)%2
a = s[l:]
b = s[:l]
print(a+b)

#Переставить два слова
Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.
s=input()
c=s.find(' ')
a=s[c+1:]
b=s[:c]
print(a+' '+b)

#Первое и последнее вхождения
Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс. Если она встречается два и более раз, выведите индекс её первого и последнего появления. Если буква f в данной строке не встречается, ничего не выводите.
s = input()
a = s.find('f')
b = s.rfind('f')
if a == -1:
    print()
elif a == b:
    print(a)
else:
    print(a, b)












