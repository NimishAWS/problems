# ------------------------  01
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5

rows = int(input("Please provide rows"))

for i in range(rows+1):
    for j in range(i):
        print(i,end=' ')
    print(' ')


# ------------------------  02

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

rows = int(input("Please provide the rows"))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')

# ------------------------  03

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

rows = int(input("Please provide the rows"))
count = 0
for i in range(rows,0,-1):
    count =  count + 1
    for j in range(1,i+1):
        print(count,end = ' ')
    print(' ')

# ------------------------  04

# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5

rows = int(input("Please provide the rows"))

for i in range(rows,0,-1):
    for j in range(0,i):
        print(rows,end = ' ')
    print(' ')

# ------------------------  04

# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1

rows = int(input("Please provide the rows"))

for i in range(rows,0,-1):
    for j in range(0,i+1):
        print(j,end = ' ')
    print(' ')


# ------------------------  04

# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9

rows  = int(input("Please provide the rows"))

for i in range(1,rows+1):
    for j in range(i):
        print(i*2-1,end =' ')
    print(' ')

i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(i*2-1,end=' ')
        j+=1
    i +=1
    print(' ')

# ------------------------  05

# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

rows = int(input("Please provide the rows"))

for i in range(rows,0,-1):
    for j in range(i):
        print(i,end = ' ')
    print(' ')

i = 1
while rows>0:
    j = 1
    while j <= rows:
        print(rows,end = ' ')
        j +=1
    rows-=1
    print(' ')

# ------------------------  05


# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1

rows = int(input("Please provide the rows"))

for i in range(0,rows+1):
    for j in range(i,0,-1):
        print(j,end = ' ')
    print(' ')

# ------------------------  06

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

rows = int(input("Please provide the rows"))

for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print(' ')

# ------------------------  07

# 1
# 3 2
# 6 5 4
# 10 9 8 7

count =0
for i in range(0,5):
    for j in range(i):
        count += 1
        print(count,end = ' ')
    print(' ')

# ------------------------  08

#           1 
#         1 2 
#       1 2 3 
#     1 2 3 4 
#   1 2 3 4 5 

rows = int(input("Please provide rows"))

for i in range(0,rows):
    count = 1
    for j in range(rows,0,-1):
        if j>i:
            print(" ",end=' ')
        else:
            print(count,end=' ')
            count += 1

    print(' ')

# ------------------------  09

# 1 2 3 4 5 
# 2 2 3 4 5 
# 3 3 3 4 5 
# 4 4 4 4 5 
# 5 5 5 5 5

rows = int(input("Please provide rows"))

for i in range(1,rows):
    for j in range(1,rows):
        if j <= i:
            print(i,end= ' ')
        else:
            print(j,end = ' ')
    print(' ')

# ------------------------  10

# 1  
# 2  4  
# 3  6  9  
# 4  8  12  16  
# 5  10  15  20  25  
# 6  12  18  24  30  36  
# 7  14  21  28  35  42  49  
# 8  16  24  32  40  48  56  64  

row = int(input("Please provide rows"))

for i in range(1,row+1):
    for j in range(1,i+1):
        print(i*j,end = " ")
    print(" ")

# ------------------------  11
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

rows = int(input("Please provide rows"))

for i in range(1,rows):
    for j in range(i):
        print("*",end= ' ')
    print(" ")

# ------------------------  12

# *  
# * *  
# * * *  
# * * * *  
#   * * * *  
#     * * *  
#       * *  
#         *  

rows = int(input("Please provide rows"))

for i in range(1,rows):
    for j in range(i):
        print("*",end= ' ')
    print(" ")
for i in range(rows):
    for j in range(rows):
        if j <= i :
            print(" ",end= " ")
        else:
            print("*",end=' ')
    print(' ')

# ------------------------  13

#           *  
#         * *  
#       * * *  
#     * * * *  
#   * * * * *  
# * * * * * * 

rows = int(input("Please provide rows"))

for i in range(rows+1):
    for j in range(rows,0,-1):
        if j >i :
            print(" ",end= " ")
        else:
            print("*",end=' ')
    print(' ')

# ------------------------  14

# * * * * *  
# * * * *  
# * * *  
# * *  
# *


row = int(input("Please provide rows"))
for i in range(row+1,0,-1):
    print("*"*i)


# ------------------------  15
# * * * * * *  
#   * * * * *  
#     * * * *  
#       * * *  
#         * *  
#           *  

rows  =  int(input("Please provide the rows"))

for i in range(rows,0,-1):
    for j in range(rows,0,-1):
        if j> i:
            print(" ",end= " ")
        else:
            print("*",end=" ")
    print(" ")

# ------------------------  16

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

rows = int(input("Please provide rows"))

for i in range(rows):
    print("*"*i,end=" ")
    print(" ")
for j in range(rows,0,-1):
    print("*"*j,end=" ")
    print(" ")