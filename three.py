'''num=int(input("Enter a Number: "))
counter=1
sum=0
while counter<= num:
    sum=sum + counter
    counter +=1
print(f"the sum is {sum} . ")'''
'''sum=0
for i in range(1, num+1):
    sum= sum+ i 
print(sum)'''
#factorial
'''def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
        


num=int(input("Enter a number"))
result= fact(num)
print(f"the factorial is {result}")
'''
#odd even counter
def odd_even_counter(n):
    counter={
        "odd": 0,
        "even": 0
    }
    for i in range(1,len(n)):
        if n[i]%2==0:
            counter["even"]+=1
        else:
            counter["odd"]+=1
    print(counter)
arr=[1,2,3,45,6,7,8,6]
odd_even_counter(arr)

