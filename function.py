# def calculation(a,b):#parameter
#     return a+b
# sum = calculation(1,4)#function call;arguments
# print(sum)
# sum = calculation(6,4)#function call;arguments
# print(sum)
# sum = calculation(9,54)#function call;arguments
# print(sum)

# name=["rahul","priya","usha","sonu"]
# cities=["indore","bhopal","pune","nashik"]
# def cal_list(list):
#     print(len(list))

# cal_list(name)
# cal_list(cities)
 
# def list(list):
#     for i in list:
#         print(i, end=" ")

# list(name)
# print()

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
        
cal_fact(3)
def cov_usd_to_inr(usd_val):
   inr_val=usd_val*83
   print(usd_val,"usd=",inr_val,"inr")

cov_usd_to_inr(23)

def Even_odd(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")

Even_odd(34)
def cal_sum(n):
    if(n==0):
        return 0
    # print(n)
    return cal_sum(n-1) + n
cal_sum(5)
print(sum)