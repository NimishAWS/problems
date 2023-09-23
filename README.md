# Problems Solving
## Hot Inteview Questions  


## Solutions In Python

1)  `Return all the repeated numbers from the list = [1,2,3,4,5,1,2,3]` 
```sh
data = [1,2,3,4,5,6,6,3,2,1]
new_data = []
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i] == data[j]:
            if data[i] not in new_data:
                new_data.append(data[i])
                
print(new_data)

Answer : [1, 2, 3, 6]
```

2)  `Return all the Prime Numbers from 1 to 100`

```sh
--------------------- Solution (1) -------------------------

n = 100
for i in range(2,n+1):
    is_prime = True
    for j in range(2,i):
        if i%j == 0: 
            is_prime=False
    if is_prime:
        print(i)
        
Answer : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

--------------------- Solution (2) -------------------------

def check_prime(number):
    for num in range(number+1):
        if num>1:
            for i in range(2,num):
                if  num%i == 0:
                    break
            else:
                print(num)
check_prime(100)

Answer : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

```

3)  `Check if the number is Prime number or Not`

```sh
--------------------- Solution (1) -------------------------

n = 97
for i in range(n,n+1):
    is_prime= True
    for j in range(2,i):
        if i%j == 0:
            is_prime =False
    if is_prime:
        print("Its prime number")
    else:
        print("Its not prime number")
        
Answer : Its prime number

--------------------- Solution (2) -------------------------

def check_prime(num):
    if num > 1:
        for i in range(2,num//2):
            if num%i == 0:
                print("No its not prime number")
                break
        else:
            print(" its prime number")
            
check_prime(95)

Answer : Its not prime number

```

4)  `Check if the string is palindrom or not`

```
--------------------- Solution (1) -------------------------

n = "nitin"
reverse_str = ""
for i in range(len(n)):
    reverse_str = n[i] +reverse_str
if reverse_str == n:
    print("Its Palindrom")
else:
    print("Its not Palindrom")
    
Answer : Its palindrom

--------------------- Solution (2) -------------------------

n ="nitin"
reverse_str = n[::-1]
if reverse_str == n:
    print("Its palindrom")
else:
    print("Its not palindrom")
    
Answer : Its palindrom

--------------------- Solution (3) -------------------------

n = "nitin"
reverse_str = "".join(reversed(n))
if reverse_str == n:
    print("Its palindrom")
else:
    print("Its not palindrom")

Answer : Its palindrom

--------------------- Solution (4) -------------------------

n="nitin"
def check_reverse(n):
    for i in range(len(n)//2):
        if n[i] == n[len(n)-1]:
            return "Its palindrom"
        return "Its not palindrom"
        
print(check_reverse(n))

Answer : Its palindrom
```

5)  `Check if the number is palindrom or not`

```
n = 1234321

def check_pal(n):
    temp = n
    reverse_num = 0

    while (temp>0):
        dig = temp%10
        reverse_num = reverse_num * 10 + dig
        temp = temp // 10
    if reverse_num == n:
        return "Its palindrom"
    else:
        return "Its not palindrom"
        
print(check_pal(n))

Answer : Its palindrom
```

6)  `Find Fibonachi series for n number`

```
--------------------- Solution (1) -------------------------

def check_fibona(n):
    a,b = 0,1
    print(a)
    while (b<n):
        print(b)
        c = a + b
        a = b
        b = c

check_fibona(50)

Answer : 0 1 1 2 3 5 8 13 21 34

--------------------- Solution (2) -------------------------

def check_fibona(n):
    a,b = 0,1
    print(a)
    while(b<n):
        print(b)
        a,b = b,a+b

check_fibona(50)

Answer : 0 1 1 2 3 5 8 13 21 34

--------------------- Solution (3) -------------------------

def feboonachi(num):
    if num <=1:
        return num
    else:
        return (feboonachi(num-1) + feboonachi(num-2))
    
n = 7
if n <= 0:
    print("Invalid")
else:
    for i in range(n):
        print(feboonachi(i))

Answer : 0 1 1 2 3 5 

--------------------- Solution (4) -------------------------

def febonacchi(num):
    a,b = 0,1
    if num == 1:
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2,num):
            c = a + b
            a = b 
            b = c
            print(c)

febonacchi(7)

Answer : 0 1 1 2 3 5 

```

7)  `Write a program which can remove a particular character from a string` 

```sh
s = input("Enter a string ")
char = input('What would you like to remove ')
result = ''
for i in s:
  if i != char:
    result = result + i

print(result)

Answer : Enter a string chetan
         What would you like to remove c
         hetan

```

8)  `Extract username from a given email. 
      Eg:- if the email is nitish24singh@gmail.com 
           then the username should be nitish24singh `
           
```sh

name = input("Enter a email ")
# user_name = name.split("@")
pos = name.index("@")
user_name =name[0:pos]

print(user_name)

Answer : Enter a email nitish24singh@gmail.com 
         nitish24singh
         
```

8)  `Compress the string x = "aaaabbbeeejjj" `
           
```sh

--------------------- Solution (1) -------------------------

x = "aaaabbbeeejjj"
count_x = ""
new_list = ""
for i in x:
    count_x = i + str(x.count(i))
    if count_x not in new_list:
        new_list += count_x
        
print(new_list)

Answer : a4b3e3j3

--------------------- Solution (2) -------------------------

x = "aaaabbbeeejjj"

def compress(x):
    temp = len(x)
    count = 1
    x_str = ""
    for i in range(temp-1):
        if x[i] == x[i+1]:
            count += 1
        else:
            x_str= x_str + x[i] + str(count)
            count = 1
    x_str= x_str + x[i] + str(count)

    print(x_str)

compress(x)

Answer : a4b3e3j3

--------------------- Solution (3) -------------------------

ch = {}
for i in x:
    if i in ch:
        ch[i] = ch[i] +1
    else:
        ch[i] = 1
new =''
for k,v in ch.items():
    new = new+ k +str(v) 
    
print(new)

Answer : a4b3e3j3

```

8)  ` create the fizz and buzz for n number . If number is divisible by 3 then write FIZZ or number is divisible by 5 then write BUZZ or if number is divisible by both 3 and 5 the write FIZZBUZZ `
           
```sh

--------------------- Solution (1) -------------------------

def fizz_buzz(num):
    for i in range(1,num+1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        
        else:
            print(i)
            
fizz_buzz(20)

Answer : None

--------------------- Solution (2) -------------------------

dic = {3:"Fizz",5:"Buzz"}

def fiz_buzz(num):
    for i in range(1,num+1):
        result = ""
        for k,v in dic.items():
            if i%k == 0:
                result = result + v
                print(result)
        if not result:
            result = i
            print(result)
                
fiz_buzz(20)

Answer : None

```
9)  ` find out least repeating charechter from string  `
           
```sh

--------------------- Solution (1) -------------------------

from collections import Counter

y = [1,2,3,4,5,1,2,3,2,1]
ch_y = Counter(y)
min_ch = min(ch_y,key=ch_y.get)
print(min_ch)

print(y.count(1))

Answer : None

--------------------- Solution (2) -------------------------

> search key 

def search_var(y,ser_chr):
    dic_char = {}
    for i in y:
        if i in dic_char:
            dic_char[i] = dic_char[i] +1
        else:
            dic_char[i] = 1
    return dic_char[ser_chr]

y = "aaabbbbeeekkkkk"   
print(search_var(y,"k"))

Answer : None

--------------------- Solution (3) -------------------------

y = "aaabbbbeeekkkkk"   
char_dic = {}
for i in y:
    if i in char_dic:
        char_dic[i] = char_dic[i] +1
    else:
        char_dic[i] = 1
min_char = min(char_dic,key=char_dic.get) 
print(min_char)

Answer : None

--------------------- Solution (4) -------------------------

y = "aaabbbbeeekkkkk"   

char_dic = {}
for i in y:
    if i in char_dic:
        char_dic[i] =char_dic[i]+1
    else:
        char_dic[i] =1
    
print(char_dic)

Answer : None

```

```

8)  ` flattern the list nested arr = [1,2,3,[4,5,[6,[9,[0,[3]]]]],7,[8,9],10]`
           
```sh

--------------------- Solution (1) -------------------------
def flat_list(nest_list):
    single_list = []
    for item in nest_list:
        if type(item) is list:
        
            single_list.extend(flat_list(item))
        else:
            single_list.append(item)
    
    return single_list
    

sing_list = flat_list(arr)
print(sing_list)

Answer : [1, 2, 3, 4, 5, 6, 9, 0, 3, 7, 8, 9, 10]


