# i=100
# while i>=1:
#     print(i)
#     i -= 1
# n=int(input("enter number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
# list=[4,5,6,7,8,9,10]
# idx=0
# while idx < len(list):
#     print(list[idx])
#     idx+=1
#
# str="hello i am prachi"
# for i in str:
#     print(i)
list=[1,2,1]
list2=list.copy()
list2.reverse()
if (list2 == list):
    print("this is palindrome")
else :
    print("Number is not Palindrom")
  