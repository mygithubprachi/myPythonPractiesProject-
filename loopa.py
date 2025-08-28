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
num =(4,9,16,25,36,49,64,81,100)
x=16
i=0
while i < len(num):
    if (num[i] == x):
        print("found at index",i)
    i += 1 