def totalamount(bill,tip):
    total=bill*(1+0.01*tip)
    total=round(total,2)
    print("the total amount is ",total)

totalamount(190,10)


#cube of a number 
def cube(num):
    return num*num*num

num=int(input("enter the number "))
print("the cube is ",cube(num))


#factorial of anynumber
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("enter the number "))
print("the factorial is ",factorial(n))