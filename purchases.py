purchases=int(input("Number of purchases: "))
while purchases<=0:
    purchases=int(input("Number of purchases: "))
tax=float(input("Sales tax: "))
while tax>1 or tax<0:
    tax=float(input("Sales tax: "))
tax+=1
customer_names=[]
item_cost=[]
i=1
while i<=purchases:
    customer=input("Customer: ")
    cost=float(input("Cost: "))
    customer_names.append(customer)
    item_cost.append(cost)
    i=i+1
def add_tax(list,t):
    i=0
    while i<=len(list)-1:
        list[i]=list[i]*t
        list[i]=round(list[i],2)
        i=i+1
add_tax(item_cost,tax)
dictionary={}
i=0
while i<=purchases-1:
    if customer_names[i] in dictionary:
        dictionary[customer_names[i]]+=item_cost[i]
    else:
        dictionary[customer_names[i]]=item_cost[i]
    i+=1
print(dictionary)

    
