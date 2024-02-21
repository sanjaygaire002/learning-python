'''wap to accept the cp of a bike and display the total road tax tpo be paid according to the following criteria
cp(in rs)       tax
>100000         15%
>50000          10%
<=50000         5%

'''
'''cost_price=int(input("Enter the cost price of the bike (In Rupees)"))
if cost_price>100000:
    tax= 0.15*cost_price
elif cost_price> 50000 and cost_price<= 100000 :
    tax= 0.10*cost_price
else :
    tax=0.5*cost_price
print(f"Your road tax is Rs.{tax} ")'''


cost_price=int(input("Enter the cost price of the bike (In Rupees)"))
t=0
def tax(cost_price):
    if cost_price>100000:
        t= 0.15*cost_price
    elif cost_price> 50000 and cost_price<= 100000 :
        t= 0.10*cost_price
    else :
        t=0.5*cost_price
    return t
r_tax= tax(cost_price)
print(f"Your road tax is Rs.{r_tax} ")