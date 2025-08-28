#print 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

#print 100 to 1
# x=100
# while x>=1:
#     print(x)
#     x-=1

#print the multiple of number n
# 
# n=int(input("enter number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
#enter a numbers in the list using loop[1,4,9,16,25,36,49,64,81,100]
# list= [1,4,9,16,25,36,49,64,81,100]
# #traverse
# idx =0
# while idx < len(list): 
#       print(list[idx])
#       idx+=1
#search for n number in tuple using loop
# num =( 1,4,9,16,25,36,49,64,81,100)
# x=16
# i=0
# while i < len(num):
   
#     if (num[i] == x):
#         print("found at index",i)
#     i += 1 

#print elements using for loop [1,4,9,16,25,36,49,64,81,100]
# list=[1,4,9,16,25,36,49,64,81,100]
# x=16
# i=0
# for num in list:
#     if(num == x):
#        print("x is found at index",i)
#     i += 1

#printnumber 1 to 100 with the help of for and range
# for num in range(1,101):
#     print(num)

#printnumber 100 to 1 with the help of for and range
# for i in range(100,0,-1):
#     print(i)

#write mul of n with the help of for and range
# n=int(input("enter number :"))
# for table in range(1,11):
#     print(table*n)

# write a pro to print sum of n number using wile loop
# n=5
# i=1
# sum=0
# while i<=n:
#     sum += i
#     i+=1
# print(sum)

# write a pro to print factors of number
# n=5
# fact=1
# for el in range(1,n+1):
#       fact*=el
# print(fact)


tup=(2,3,2,4,5,6,7,5,8,9,10,24,"kuldip loves butkis")
list3=list(tup)
# Separate numbers only
list3 = [x for x in tup if isinstance(x, int)]

list3.sort()

tup=list3
print(tup.count(2),"this is value ot tuple",tup.count(10))
x=5
i=0
print("The lengh of tuple is ->" , len(tup))
while i < len(tup):
      if (tup[i]==x):
          print("found at",i)
      i+=1