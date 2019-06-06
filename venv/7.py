#OPERATORS
#arthmatic operators

dish1=100
dish2=200
bill=dish1+dish2
print("bill is:",bill)
# +,-,*,/,//,**
taxes=.05*bill
print(taxes)

totalbill=bill+taxes
print("toal amount:",totalbill)

num1=10
num2=3
num3=num1//num2
print(num3)
num3=num1**num2
print(num3)

#assignment operators
num1=10
num1=5

num2=num1 #copyoperation| reference copy

#num1+=5
print(num1)

# *=,/=,//=,*=,**=
num1**=2
num1//=2
print(num1)



#comparison operators
p=234
p2=6565
print("are votes equal" , p==p2)
print("hgsjgsf",p>p2)


#logical oprators
p=70
c=90
m=80
print("okokokokokoko",(m>p and m>c))

# not -> explore



#bitwise operators
a=8
b=12
c=a&b
print(c)
c=a|b
print(c)
c=a^b
print(c)

"""
x=12
y=3
#shift operation
#z=x>>y
z=x<<y
print(z)
"""

x=-13
y=2
z=x>>y
print(z)


# identity and membership operations
n1=10
n2=10
""""
print(n1==n2)
print(n1 is n2)

both are same
"""

roll=[1,2,3,4,5]
print(4 in roll)
print(20 not in roll)

#explore membership operators on tuple,set and dictonary



#conditional constructs
total=10
"""
if total >=500:
    print("flat 40% off")
else:
    print("no discount")
"""
if total>=100 and total<200:
    print(flat20% off)
elif total>=200 and total <300:
    print("flat30% off")
elif total>=500:
    print("flat50%off")
else:
    print("100 ke uper ka kr order discount chahiye toh")

#nested if/else
isInternetconnected= True
isGpsconnected= False

if isInternetconnected:
    print("you can browse")
    if isGpsconnected:
        print("naigate")
    else :
        print("no")
else:
    print("try again")

#code same for amazon/zomato/whatsapp



#loops
number= int(input("enter a number: "))

for i in range(0,20,2):
    print(i)
"""
while i<=10:
    print(number, 1, "s are", (number * i))
    i += 1
"""






