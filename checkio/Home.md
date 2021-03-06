#### 1. Sum Numbers
Sum the numbers.
```
def sum_numbers(text: str) -> int:
    return sum(int(i) for i in text.split() if i.isdigit())
```

#### 2. Even The Last
How to work with arrays indexes.
```
def checkio(array: list) -> int:
    m=0
    if len(array)==0:
        return m
    sum=0
    for i in range(0,len(array),2):
        sum+=array[i]
        m=sum*array[len(array)-1]
    return m
```
**best:**
```
def checkio(array: list) -> int:
    result = sum([num for num in array[::2]]) * array[-1] if array else 0
    return result
```

#### 3. Right to Left
You are given a sequence of strings. You should join these strings into a chunk of text where the initial strings are separated by commas. As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.
```
def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    return (','.join(phrases)).replace('right','left')
```
#### 4. Right to Left
How to discern words and numbers.
```
def checkio(words: str) -> bool:
    с = 0
    for word in words.split():
        if word.isalpha():
            с += 1
        else:
            с = 0
        if c == 3:
            return True
    return False
```

#### 5. First Word
Find the first word in a string
```
def first_word(text: str) -> str:
    t=text.replace('.' ,' ')
    t1=t.replace(',',' ')
    t2=t1.split()
    return t2[0]
```
#### 6. Days Between
How many days old are you? I’m 7,665, but my license says 14,600...
```
def days_diff(a, b):
    import datetime
    return abs((datetime.date(*a)-datetime.date(*b)).days)
```
#### 7. Count Digits
```
def count_digits(text: str) -> int:
    c=0
    for i in list(text):
        if i.isdigit():
            c+=1
    return c
```
**best:**
```
def count_digits(text: str) -> int:
    return sum(c.isdigit() for c in text)
```
#### 8. Backward Each Word
Reverse every word in a given line
```
def backward_string_by_word(text: str) -> str:
    return " ".join([i[::-1] for i in text.split(" ")])
```
#### 9. Bigger Price
Find TOP most expensive goods.
```
def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    return sorted(data, key=lambda x: x['price'], reverse=True) [:limit]
```
#### 10. Between Markers
find a substring between markers
```
def bigger_price(limit: int, data: list) -> list:
    """
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    if begin in text and end in text:
        begind=text.find(begin)+len(begin)-1
        endind=text.find(end)
        return text[begind+1:endind]
        if begind<endind:
            return ''
    if begin not in text and end in text:
        endind=text.find(end)
        return text[:endind]
    if begin in text and end not in text:
        begind=text.find(begin)+len(begin)
        return text[begind:]
    if begin and end not in text:
        return text
```
**best:**
```
def between_markers(text: str, begin: str, end: str) -> str:
    b, e = text.find(begin), text.find(end)
    return text if b == e == -1 else text[:e] if b == -1 else text[b+len(begin):] if e == -1 else text[b+len(begin):e]    
```
#### 11. Non-unique Elements
Trim an array down to its non-unique elements
```
def checkio(data: list) -> list:
    res = []
    for i in data:
        if data.count(i)>1:
            res.append(i)
    return res
```
**best:**
```
def checkio(data: list) -> list:
    return [n for n in data if data.count(n) > 1]
```
#### 12. Popular Words
Determine the words' popularity.
```
def popular_words(text: str, words: list) -> dict:
    enddict={}
    newt=text.lower().split()
    for i in words:
        enddict[i]=newt.count(i)
    return enddict
```
**best:**
```
def popular_words(text: str, words: list) -> dict:
    split = text.lower().split()
    return {w: split.count(w) for w in words}
```



#### 13. Second Index
```
def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol)<=2:
        if text.count(symbol)>1:
            r=text.rfind(symbol)
        else:
            r=None
    else:
        r=(text[:text.find(symbol)]+text[text.find(symbol)+1:]).find(symbol)+1

    return r
```
#### 14. Split List
Split an array into two arrays.
```
def split_list(items: list) -> list:
    from math import ceil,floor
	items1=[]
	items2=[]
	if len(items)%2==0:
		items1.extend(items[:int(len(items)/2)])
		items2.extend(items[int(len(items)/2):])
	else:
		items1.extend(items[:ceil(len(items)/2)])
		items2.extend(items[ceil(len(items)/2):])
	return [items1]+[items2]
```
#### 15. All the Same
Check if all elements are the same?
```
def all_the_same(elements: List[Any]) -> bool:
    return elements.count(elements[0])==len(elements) if len(elements)!=0 else True
```
