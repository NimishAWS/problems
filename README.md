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
n = 100
for i in range(2,n+1):
    is_prime = True
    for j in range(2,i):
        if i%j == 0: 
            is_prime=False
    if is_prime:
        print(i)
        
Answer : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

3)  `Check if the number is Prime number or Not`

```sh
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
```






