a=int(input("enter 3 digit number"))
b=a//100
c=a%100
d=c//10
e=c%10
e=c**3+b**3+a**3
if a==0:
    print("armstrong")
else:
    print("not armstrong")