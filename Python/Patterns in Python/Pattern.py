#write a py prog to understand pattern


#Pattern:-
# *****
# ****
# ***
# **
# *
n=int(input("Enter A Number "))
for i in range(n+1):
    for j in range(1,(n+1)-i):
        print("*",end="")
    print()
print()
print()


#Pattern:-
# *****
#  ****
#   ***
#    **
#     *
for i in range(n+1):
    for j in range(1,(i+1)):
        print(" ",end="")
    for k in range(i,n):
        print("*",end="")
    print()
print()
print()



#Pattern:-
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
for i in range(n+1):
    for j in range(1,(i+1)):
        print(" ",end="")
    for k in range(i,n):
        print("*",end=" ")
    print()
print()
print()


#Pattern:-
#     *
#    **
#   ***
#  ****
# *****
for i in range(1,n+1):
    for j in range(1,(n+1-i)):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()
print()
print()



#Pattern:-
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
for i in range(1,n+1):
    for j in range(1,(n+1-i)):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
print()
print()


#Pattern:-
# 1
# 01
# 101
# 0101
# 10101
for i in range(1,n+1):
    for j in range(1,(i+1)):
        print((i+j-1)%2,end="")
    print()
print()
print()



#Pattern:-
# 1
# 23
# 456
# 759
# 101112
k=1
for i in range(1,n+1):
    for j in range(1,(i+1)):
        print(k,end="")
        k+=1
    print()
print()
print()
