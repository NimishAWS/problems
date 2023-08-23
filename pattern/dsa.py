
def reversed_str(string):
    string = string.lower()
    reverse_str = ""
    for i in string:
        reverse_str = i + reverse_str
    
    if reverse_str == string:
        return "Palindrom"
    else:
        return "its not palindrom"
        
        
print((reversed_str("Nitin")))

def reversed_str2(string):
    string = string.lower()
    
    check = "".join(reversed(string))
    if check == string:
        return "Palindrom"
    else:
        return "its not palindrom"
    
print((reversed_str2("Nimish")))

def reverse_num(num):
    in_num = num
    rev_num = 0
    while num > 0:
        last_digit = num %10
        rev_num = (rev_num*10)+last_digit
        num = num // 10

    if rev_num == in_num:
        print("its palindrom")
    else:
        print("its not palindrom")
print(reverse_num(121))

def reverse_sentence(string):
    # reverse = " ".join(reversed(string.split())) # solution 1
    reverse = " ".join(string.split()[::-1])
    return reverse

print(reverse_sentence("Hello this is Nimish"))

def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
n = 9
count = 0
if n <= 0:
    print("Invalid")
else:
    for i in range(n):
        if count == 5:
            break
        print(fibo(i))
        count += 1
        
def reversal_word(string):
    n = string.split()
    print(n)
    sen = " "
    for i in n:
        print(i)
        sen = i + " " +sen
    
    print(sen)
    
print(reversal_word("Nimish working or not"))


def comprres_string(string):
    count = {}
    one_str = ""
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i,j in count.items():
        one_str =one_str +str(i)+str(j)
    return one_str
    
    

print(comprres_string("AAAAddddEEEwwww"))




def unique_char(string):
    char = set()
    for i in string:
        if i in char:
            return False
        else:
            char.add(i)
    return True
    
print(unique_char("abcd"))



class Stack(object):
    
    def __init__(self):
        self.item = []
        
    def push(self,item):
        self.item.append(item)
        
    def pop(self):
        self.item.pop()
        
    def isEmpty(self):
        self.item == []
    
    def size(self):
        return len(self.item)
        
    def peek(self):
        return self.item[len(self.item) - 1]
        
class Queue(object):
    def __init__(self):
        self.item = []
        
    def enqueue(self,item):
        self.item.insert(0,self.item)
    
    def denqueue(self):
        self.item.pop()
        
    def size(self):
        return self.item(len(self.item))
        
        
class Deqeue(object):
    def __init__(self):
        self.item = []
        
    def __str__(self):
        return self.item
        
    def isEmpty(self):
        return self.item == []
        
    def addFront(self,item):
        self.item.append(item)
        
    def addRear(self,item):
        self.item.insert(0,item)
        
    def removeFront(self):
        return self.item.pop()
        
    def removeRear(self):
        return self.item.pop(0)
    
    def size(self):
        return len(self.item)
        
print(Deqeue)

obj3 = Deqeue()

obj3.addFront("Nimish")
obj3.addRear("Nagapure")
print(obj3.size())
print(obj3.removeFront() + " " + obj3.removeFront())
print(obj3.size())
print(obj3.isEmpty())


# print(obj3)







value = '{{{{(((())))}}}}[[]]'

def check_para(string):
    count = 0
    for i in string:
        if i == "{":
            count += 1
        if i == "}":
            count -= 1
        if i == "(":
            count += 1
        if i == ")":
            count -= 1
        if i == "[":
            count += 1
        if i == "]":
            count -= 1
    if count == 0:
        return True
    else:
        return False
        
print(check_para(value))


def two_pair(arry,target):
    count= {}
    pair = []
    
    for i in arry:
        comp = target - i
        if comp in count:
            pair.append((comp,i))
        count[i] = True
        
    return pair

arr = [1,2,4,3,5,7,9]   
print(two_pair(arr,3))
        
        
            
        
